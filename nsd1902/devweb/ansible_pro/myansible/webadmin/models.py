from django.db import models

# Create your models here.

class HostGroup(models.Model):
    groupname = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.groupname

class Host(models.Model):
    hostname = models.CharField(max_length=100, unique=True)
    ipaddr = models.CharField(max_length=15)
    group = models.CharField(HostGroup)

    def __str__(self):
        return '%s=>%s' % (self.group, self.hostname)

class Module(models.Model):
    module_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.module_name

class Args(models.Model):
    arg_text = models.CharField(max_length=100)
    module = models.ForeignKey(Module)

    def __str__(self):
        return '%s=>%s' % (self.module, self.arg_text)
