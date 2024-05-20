# Generated by Django 5.0.1 on 2024-05-13 08:01

import taggit.managers
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_alter_picture_image_tag'),
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
    ]

    operations = [
        migrations.AddField(
            model_name='picturebook',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
