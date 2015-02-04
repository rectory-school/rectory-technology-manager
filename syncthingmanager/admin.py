from django.contrib import admin
from syncthingmanager import models

class FolderPathInline(admin.StackedInline):
  model = models.FolderPath
  filter_horizontal = ["folders"]
  
  extra = 0

class ManagedDeviceAdmin(admin.ModelAdmin):
  inlines = [FolderPathInline]

class SubDeviceAdmin(admin.ModelAdmin):
  filter_horizontal = ["folders"]

class FolderAdmin(admin.ModelAdmin):
  fields = ['name', 'relative_path', 'folderPaths', 'stubDevices']
  readonly_fields = ('folderPaths', 'stubDevices')

  def folderPaths(self, o):
    return ", ".join(map(str, models.FolderPath.objects.filter(folders=o)))
    
  def stubDevices(self, o):
    return ", ".join(map(str, models.StubDevice.objects.filter(folders=o)))
  
  folderPaths.short_description = "Managed devices"
  stubDevices.short_description = "Client devices"
    
# Register your models here.
admin.site.register(models.ManagedDevice, ManagedDeviceAdmin)
admin.site.register(models.Folder, FolderAdmin)
admin.site.register(models.StubDevice, SubDeviceAdmin)