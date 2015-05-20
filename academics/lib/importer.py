from academics.models import StudentPermRec
import xml.etree.ElementTree as ET
from django.db import transaction
import logging

logger = logging.getLogger(__name__)

def importPermRecs(permRecFile):
  root = ET.parse(permRecFile).getroot()
  data = xmlToDict(root)
  
  BASICDATAMAP = {
    'NameFirst': 'first_name',
    'NameLast': 'last_name',
    'NameNickname': 'nickname',
    'EMailSchool': 'email'
  }
  
  ksAllStudentIDs = set([d['IDSTUDENT'] for d in data])
  seenStudentIDs = set()
  
  changedCount = 0
  
  with transaction.atomic():
    #New and updated records
    for ksRecord in data:
      seenStudentIDs.add(ksRecord['IDSTUDENT'])
      
      changed = False
      
      try:
        tmObject = StudentPermRec.objects.get(student_id=ksRecord['IDSTUDENT'])
      except StudentPermRec.DoesNotExist:
        logger.info('Creating student with ID {student_id}'.format(student_id=ksRecord['IDSTUDENT']))
        tmObject = StudentPermRec()
        tmObject.student_id = ksRecord['IDSTUDENT']
        changed = True
      
      for ksFieldName, tmFieldName in BASICDATAMAP.items():
        ksValue = (ksRecord[ksFieldName] or "").strip()
        tmValue = getattr(tmObject, tmFieldName)
        
        if ksValue != tmValue:
          logger.info("Updating field {field} from '{old}' to '{new}' on student id {student_id}".format(field=tmFieldName, old=tmValue, new=ksValue, student_id=tmObject.student_id))
          setattr(tmObject, tmFieldName, ksValue)
          changed = True
      
      if changed:
        changedCount += 1
        tmObject.save()
    
    #Extra records
    extraRecords = StudentPermRec.objects.exclude(student_id__in=seenStudentIDs)
    for record in extraRecords:
      logger.warn("Removing student perm rec record {id} with student id {student_id}".format(id=record.id, student_id=record.student_id))
      record.delete()

    
        

def xmlToDict(root):
  metadata = root.find('{http://www.filemaker.com/fmpxmlresult}METADATA')
  resultSet = root.find('{http://www.filemaker.com/fmpxmlresult}RESULTSET')
  fields = []

  for child in metadata.findall('{http://www.filemaker.com/fmpxmlresult}FIELD'):
    fields.append(child.get("NAME"))

  data = []

  for row in resultSet:
    out = {}
    for i in range(len(fields)):
      value = row[i][0].text
      out[fields[i]] = value

    data.append(out)

  return data