# Generated by Django 2.2 on 2021-02-04 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coffees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.CharField(max_length=255, null=True)),
                ('roast', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('email', models.CharField(max_length=60)),
                ('street_address', models.CharField(max_length=255)),
                ('address_two', models.CharField(max_length=255, null=True)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=2)),
                ('zip_code', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SingleCartItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ordered_coffee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coffee_selected', to='Flight_School_Coffee_app.Coffees')),
            ],
        ),
        migrations.CreateModel(
            name='TotalCartItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cart_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shopping_cart', to='Flight_School_Coffee_app.SingleCartItems')),
                ('ordered_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='Flight_School_Coffee_app.Customers')),
            ],
        ),
        migrations.CreateModel(
            name='Styles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style_name', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('style_for_coffee', models.ManyToManyField(related_name='coffee_style', to='Flight_School_Coffee_app.Coffees')),
            ],
        ),
        migrations.CreateModel(
            name='Sizes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_size', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('size_for_coffee', models.ManyToManyField(related_name='coffee_size', to='Flight_School_Coffee_app.Coffees')),
            ],
        ),
        migrations.AddField(
            model_name='singlecartitems',
            name='ordered_size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='size_selected', to='Flight_School_Coffee_app.Sizes'),
        ),
        migrations.AddField(
            model_name='singlecartitems',
            name='ordered_style',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='style_selected', to='Flight_School_Coffee_app.Styles'),
        ),
    ]
