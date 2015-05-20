from django.core.management.base import BaseCommand, CommandError
from academics.lib.importer import importPermRecs
class Command(BaseCommand):
  args = 'permrecs_file'
  help = 'Imports permrecs data'

  def handle(self, *args, **options):
    if len(args) != 1:
      raise CommandError('Argument must be path to the perm recs file')
    
    permRecsPath = args[0]
    
    f = open(permRecsPath, "rb")
    
    importPermRecs(f)
    f.close()