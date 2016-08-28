from django.db import models
from autoslug import AutoSlugField
from PIL  import Image
from cStringIO import StringIO
from django.core.files.uploadedfile import SimpleUploadedFile
import os


class Picture(models.Model):
    file = models.ImageField(upload_to="pictures")
    name = models.CharField(max_length=100, null=True, blank=True)
    thumbnail = models.ImageField(upload_to="pictures/thumbs", max_length=500, blank=True, null=True)
    slug = AutoSlugField(populate_from='name')

    @models.permalink
    def get_absolute_url(self):
        return 'picture', (), {'slug': self.slug}

    def delete(self, *args, **kwargs):
        self.file.delete(False)
        super(Picture, self).delete(*args, **kwargs)

    def create_thumbnail(self):
        if not self.file:
            return

        # Set our max thumbnail size in a tuple (max width, max height)
        THUMBNAIL_SIZE = (200, 200)

        DJANGO_TYPE = self.file.file.content_type
        print DJANGO_TYPE
        if DJANGO_TYPE == 'image/jpeg':
            PIL_TYPE = 'jpeg'
            FILE_EXTENSION = 'jpg'
        elif DJANGO_TYPE == 'image/png':
            PIL_TYPE = 'png'
            FILE_EXTENSION = 'png'

        # Open original photo which we want to thumbnail using PIL's image
        uploaded_file = Image.open(StringIO(self.file.read()))

        uploaded_file.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)

        # Save the thumbnail
        temp_handle = StringIO()
        uploaded_file.save(temp_handle, PIL_TYPE)
        temp_handle.seek(0)
        print temp_handle

        # Save uploaded_file to a SimpleUploadedFile which can be saved into
        # ImageField
        suf = SimpleUploadedFile(os.path.split(self.file.name)[-1],
                                 temp_handle.read(), content_type=DJANGO_TYPE)
        print suf
        # Save SimpleUploadedFile into uploaded_file field
        self.thumbnail.save('%s_thumbnail.%s' % (os.path.splitext(suf.name)[0], FILE_EXTENSION), suf, save=False)

    def save(self, *args, **kwargs):
        self.create_thumbnail()
        self.slug = self.name

        super(Picture, self).save(*args, **kwargs)
