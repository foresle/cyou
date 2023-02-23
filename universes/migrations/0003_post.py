# Generated by Django 4.1.7 on 2023-02-22 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('universes', '0002_universe_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='A New Post', max_length=120)),
                ('payload', models.CharField(max_length=6000)),
                ('universe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='universe_posts', to='universes.universe')),
            ],
        ),
    ]
