# Generated by Django 2.1.5 on 2019-01-27 07:44

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=20)),
                ('pin_code', models.CharField(max_length=6)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=13)),
                ('residence', models.CharField(max_length=50)),
                ('locality', models.CharField(max_length=60)),
                ('landmark', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('district', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(choices=[('Uttar Pradesh', 'Uttar Pradesh'), ('Delhi', 'Delhi'), ('Punjab', 'Punjab')], default='', max_length=30)),
                ('country', models.CharField(choices=[('India', 'India')], default='India', max_length=15)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OTP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp', models.IntegerField()),
                ('sent_on', models.DateTimeField(auto_now_add=True)),
                ('receiver', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PickupAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company_name', models.CharField(max_length=50)),
                ('pin_code', models.CharField(max_length=6)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=13)),
                ('full_address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(choices=[('Uttar Pradesh', 'Uttar Pradesh'), ('Delhi', 'Delhi'), ('Punjab', 'Punjab')], default='', max_length=30)),
                ('country', models.CharField(choices=[('India', 'India')], default='India', max_length=15)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('image', models.ImageField(default='product_pics/download.png', upload_to='product_pics')),
                ('video', models.FileField(blank=True, null=True, upload_to='product_videos')),
                ('category', models.CharField(blank=True, choices=[('electronics', 'Electronics'), ('decorations', 'Decorations'), ('men wears', 'Men Wears'), ('women wears', 'Women Wears'), ('kids', 'Kids'), ('groceries', 'Groceries'), ('cosmetics', 'Cosmetics'), ('books', 'Books'), ('furnitures', 'Furnitures')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.PositiveSmallIntegerField(choices=[(1, 'buyer'), (2, 'seller')], primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='SellerDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=20)),
                ('bank_account_no', models.BigIntegerField()),
                ('IFSC_code', models.CharField(max_length=11)),
                ('aadhar_no', models.BigIntegerField(null=True)),
                ('pan_card_no', models.CharField(blank=True, max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('electronics', models.CharField(blank=True, choices=[('mobile', 'Mobile'), ('Laptop', 'Laptop'), ('earphone', 'Earphone'), ('speaker', 'Speaker'), ('air_conditioner', 'Air Conditioner'), ('washing_machine', 'Washing Machine'), ('water_pump', 'Water Pump'), ('hair_drier', 'Hair Drier'), ('projector', 'Projector'), ('desktop', 'Desktop'), ('cpu', 'CPU'), ('mouse', 'Mouse'), ('keyboard', 'Keyboard'), ('other', 'Other')], max_length=30, null=True)),
                ('decorations', models.CharField(blank=True, choices=[('vase', 'Vase'), ('painting', 'Painting'), ('statue', 'Statue'), ('curtain', 'Curtain'), ('bedsheet', 'Bedsheet')], max_length=30, null=True)),
                ('men_wears', models.CharField(blank=True, choices=[('shirt', 'Shirt'), ('t-shirt', 'T-shirt'), ('jeans', 'Jeans'), ('pant', 'Pant'), ('trouser', 'Trouser'), ('jacket', 'Jacket'), ('suit', 'Suit')], max_length=30, null=True)),
                ('women_wears', models.CharField(blank=True, choices=[('top', 'Top'), ('jeans', 'Jeans'), ('saari', 'Saari'), ('lehnga', 'Lehnga'), ('t-shirt', 'T-shirt'), ('suit', 'Suit'), ('salwar', 'Salwar')], max_length=30, null=True)),
                ('kids', models.CharField(blank=True, choices=[('cap', 'Cap'), ('shirt', 'Shirt'), ('inner_wear', 'Inner Wear'), ('diaper', 'Diaper'), ('t-shirt', 'T-shirt'), ('half-pant', 'Half Pant'), ('full-pant', 'Full Pant'), ('bottle', 'Bottle')], max_length=30, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.Subcategory'),
        ),
        migrations.AddField(
            model_name='product',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='roles',
            field=models.ManyToManyField(to='accounts.Role'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
