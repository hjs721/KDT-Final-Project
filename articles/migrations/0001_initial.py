# Generated by Django 3.2.13 on 2022-12-07 01:02


from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CatArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('암컷', '암컷'), ('수컷', '수컷')], max_length=20)),
                ('hits', models.IntegerField(default=0)),
                ('memo', models.CharField(max_length=20)),
                ('neutered', models.BooleanField(default=False, verbose_name='중성화 했나요?')),
                ('vaccination', models.BooleanField(default=False, verbose_name='예방접종 했나요?')),
                ('bookmarks', models.ManyToManyField(related_name='catarticle_bookmark', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CatCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='DogArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('암컷', '암컷'), ('수컷', '수컷')], max_length=20)),
                ('hits', models.IntegerField(default=0)),
                ('memo', models.CharField(max_length=20)),
                ('neutered', models.BooleanField(default=False, verbose_name='중성화 했나요?')),
                ('vaccination', models.BooleanField(default=False, verbose_name='예방접종 했나요?')),
                ('bookmarks', models.ManyToManyField(related_name='dogarticle_bookmark', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DogCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='DogArticleComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('dogarticle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.dogarticle')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='dogarticle',
            name='dog_breed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.dogcategory'),
        ),
        migrations.AddField(
            model_name='dogarticle',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='CatArticleComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('catarticle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.catarticle')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='catarticle',
            name='cat_breed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.catcategory'),
        ),
        migrations.AddField(
            model_name='catarticle',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
