# Generated by Django 3.2.12 on 2022-07-07 19:15

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PullRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('branch_source', models.CharField(max_length=50)),
                ('branch_destiny', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=500)),
                ('status', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
