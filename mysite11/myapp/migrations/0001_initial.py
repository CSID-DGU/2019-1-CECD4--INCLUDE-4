# Generated by Django 2.2.4 on 2019-09-27 08:54

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client_info',
            fields=[
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
                ('client_code', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('cl_email', models.CharField(blank=True, max_length=10)),
                ('cl_phone', models.CharField(blank=True, max_length=11)),
                ('auth', models.BooleanField(default=False)),
                ('passport', models.CharField(blank=True, max_length=10)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
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
            name='Company_info',
            fields=[
                ('Company_code', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('Company_name', models.CharField(blank=True, max_length=100)),
                ('President_Email', models.EmailField(max_length=254)),
                ('Address', models.CharField(blank=True, max_length=100)),
                ('information', models.CharField(blank=True, max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='TokenList',
            fields=[
                ('tokenname', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('compname', models.CharField(max_length=100)),
                ('CUR_price', models.FloatField(default=0)),
                ('Contractadress', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='tokensell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tokenname', models.CharField(max_length=100)),
                ('quota', models.FloatField(default=0)),
                ('price', models.FloatField(default=0)),
                ('token_seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tokenchange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tokenprice', models.FloatField(default=0)),
                ('quantity', models.FloatField(default=0)),
                ('seller', models.CharField(max_length=100)),
                ('buyer', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('T_type', models.CharField(max_length=3)),
                ('Approval', models.BooleanField(default=False)),
                ('tokenname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.TokenList')),
            ],
        ),
        migrations.CreateModel(
            name='Token_Trans',
            fields=[
                ('Time', models.DateTimeField(primary_key=True, serialize=False, verbose_name='date publised')),
                ('price', models.FloatField(default=0)),
                ('company_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Company_info')),
            ],
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.CharField(max_length=100)),
                ('quantity', models.FloatField(default=0)),
                ('tokenname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.TokenList')),
            ],
        ),
        migrations.CreateModel(
            name='Client_account',
            fields=[
                ('Account_code', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('Quota', models.FloatField(default=0)),
                ('Cli_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
                ('Company_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Company_info', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='buytoken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tokenname', models.CharField(max_length=100)),
                ('quota', models.FloatField(default=0)),
                ('price', models.FloatField(default=0)),
                ('token_taker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]