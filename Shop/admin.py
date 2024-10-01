from django.contrib import admin
from .models import Cart, CartItem, Menu, Order, OrderItem, User

# Admin untuk model OrderItem
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1  # Tambahkan satu form kosong untuk item baru dalam pesanan

# Admin untuk model Order
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_price', 'status', 'payment_status', 'delivery_time')  # Tampilkan informasi penting tentang pesanan
    list_filter = ('status', 'payment_status')  # Filter berdasarkan status dan pembayaran
    search_fields = ('user__name', 'id')  # Fungsi pencarian berdasarkan nama user atau ID order
    readonly_fields = ('order_time',)  # Membuat order_time hanya-baca di admin
    inlines = [OrderItemInline]  # Menambahkan OrderItem sebagai inline untuk Order

    # Custom save_model untuk mengosongkan Cart setelah Order dibuat
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)  # Menyimpan order terlebih dahulu
        try:
            # Mengambil keranjang user terkait
            cart = Cart.objects.get(user=obj.user)
        except Cart.DoesNotExist:
            # Jika keranjang tidak ditemukan, berikan log atau pesan error yang sesuai
            self.message_user(request, f"Cart for user {obj.user.name} not found.", level="error")
            return  # Menghentikan eksekusi jika tidak ada keranjang
          
        # Mengambil cart user terkait
        cart = Cart.objects.get(user=obj.user)

        # Memindahkan semua item dari Cart ke OrderItem
        for cart_item in cart.items.all():
            OrderItem.objects.create(
                order=obj,
                menu=cart_item.menu,
                quantity=cart_item.quantity,
                price=cart_item.menu.price * cart_item.quantity
            )

        # Mengosongkan Cart setelah Order dibuat
        cart.items.all().delete()  # Menghapus semua item di Cart
        cart.delete()  # Menghapus keranjang pengguna

# Admin untuk model Cart
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')  # Menampilkan user dan tanggal pembuatan di daftar admin

# Admin untuk model Menu
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')  # Menampilkan nama, harga, dan deskripsi menu
    search_fields = ('name',)  # Menambahkan fungsi pencarian berdasarkan nama

# Admin untuk model User
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'phone_number')  # Menampilkan email, nama, dan nomor telepon di daftar admin
    search_fields = ('email', 'name')  # Fungsi pencarian berdasarkan email dan nama

# admin untuk CartItem
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'menu', 'quantity')

# admin untuk OrderItem
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'menu', 'quantity', 'price')

# Registrasi model ke admin
admin.site.register(Cart, CartAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(User, UserAdmin)
# model CartItem dan OrderItem di admin
admin.site.register(CartItem, CartItemAdmin)
admin.site.register(OrderItem, OrderItemAdmin)