from __future__ import unicode_literals

from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.db import models

class CommentManager(models.Manager):
    """Comment manager is a manager for all comment objects.

    """
    def all(self):
        """Returns all comments
        qs: all comment objects
        """
        qs = super(CommentManager, self).filter(parent = None)
        return qs


    def filter_by_instance(self, instance):
        """
        returns all comments within a particular instance (page for example)
        """
        content_type = ContentType.objects.get_for_model(instance.__class__)
        obj_id = instance.id
        qs = super(CommentManage, self).filter(content_type= content_type, object_id = obj_id).filter(parent = None)
        return qs

class Comment(models.Model):
    """
    The comment object which shows the complex

    Attributes:
        user: ForeignKey to the user object
        content_type: ForeignKey to return the type of object
        object_id: integer that represents the ID of the comment
        content_object: ForeinKey that contains both content type and object_id
        parent: reference to comment object if this comment is a reply
        content: the text in the comment itself
        timestamp: the time the comment was made

    """
    user            = models.ForeignKey(settings.AUTH_USER_MODEL, default =1)
    content_type    = models.ForeignKey(ContentType, on_delete = models.CASCADE)
    object_id       = models.PositiveIntegerField()
    content_object  = GenericForeignKey('content_type', 'object_id')
    parent          = models.ForeignKey("self", null=True,  blank = True)

    content         = models.TextField()
    timestamp       = models.DateTimeField(auto_now_add = True)

    objects = CommentManager()

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return str(self.user.username)

    def get_absolute_url(self):
        return reverse("comments:thread", kwargs = {"id": self.id})

    def get_delete_url(self):
        return reverse("comments:delete", kwargs = {"id":self.id})

    def children(self):
        return Comment.objects.filter(parent = self)

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True
