from django.core.management.base import BaseCommand
from django_seed import Seed
from Shop.models import User, Menu, Cart, CartItem
from faker import Faker
import random

class Command(BaseCommand):
    help = "Seed the database with dummy data"

    def handle(self, *args, **kwargs):
        seeder = Seed.seeder()
        fake = Faker()

        # Seed Users
        seeder.add_entity(User, 10, {
            'email': lambda x: fake.unique.email(),
            'name': lambda x: fake.name(),
            'phone_number': lambda x: fake.phone_number(),
            'address': lambda x: fake.address(),
            'password': lambda x: fake.password(),
        })

        # Seed Menu items
        seeder.add_entity(Menu, 20, {
            'name': lambda x: fake.word(),
            'description': lambda x: fake.text(),
            'image_url': lambda x: fake.image_url(),
            'price': lambda x: round(random.uniform(10.00, 100.00), 2),
        })

        # Execute seeder for User and Menu
        inserted_pks = seeder.execute()

        # Create carts and cart items manually
        users = User.objects.all()
        menus = Menu.objects.all()

        for user in users:
            cart = Cart.objects.create(user=user)

            for _ in range(random.randint(1, 5)):
                menu = random.choice(menus)
                CartItem.objects.create(
                    cart=cart,
                    menu=menu,
                    quantity=random.randint(1, 5),
                )

        # # Create orders manually
        # for user in users:
        #     if random.choice([True, False]):
        #         total_price = 0
        #         cart_items = CartItem.objects.filter(cart__user=user)
                
        #         order = Order.objects.create(
        #             user=user,
        #             total_price=0,  # We'll calculate the total price below
        #             delivery_address=fake.address(),
        #             delivery_time=fake.future_datetime(),
        #             status='pending',
        #             payment_status='unpaid',
        #         )

        #         for item in cart_items:
        #             order_item = OrderItem.objects.create(
        #                 order=order,
        #                 menu=item.menu,
        #                 quantity=item.quantity,
        #                 price=item.menu.price * item.quantity
        #             )
        #             total_price += order_item.price
                
        #         order.total_price = total_price
        #         order.save()

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database with dummy data!'))
