from rest_framework import serializers
from apis.models import Schools, StudentSubjectsScore, Personnel,Subjects,Classes,SchoolStructure



class GetFullName(serializers.Field):
    def to_representation(self, obj):
        return '%s %s' %(obj.first_name, obj.last_name)


class getGrade(serializers.Field):
    def to_representation(self, obj):
        if(obj.score >= 80 and obj.score <= 100 ):
            return 'A' 
        elif(obj.score >= 75 and obj.score < 80 ):
            return 'B+' 
        elif(obj.score >= 70 and obj.score < 75 ):
            return 'B' 
        elif(obj.score >= 65 and obj.score < 70 ):
            return 'C+' 
        elif(obj.score >= 60 and obj.score < 65 ):
            return 'C' 
        elif(obj.score >= 55 and obj.score < 60 ):
            return 'D+' 
        elif(obj.score >= 50 and obj.score < 55 ):
            return 'D' 
        else:
            return 'F'
        
class SchoolSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Schools
        fields = ['id','title']

class getPersonnelType(serializers.Field):
    def to_representation(self, obj):
        if(obj.personnel_type == 0):
            return 'Teacher'
        if(obj.personnel_type == 1):
            return 'Head of the room'
        else:
            return 'Student'
class getSchoolTitle(serializers.Field):
    def to_representation(self, obj):
        return obj.school_class.school.title
class getClass(serializers.Field):
    def to_representation(self, obj):
        return obj.school_class.class_order
            
class ClassessSerializers(serializers.ModelSerializer):
    school = SchoolSerializers(many=True,read_only=True)
    class Meta:
        model = Classes
        fields = ('__all__')
        
class SubjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = ('title',)

class SubjectDetailSerializers(serializers.ModelSerializer):
    subjects = SubjectSerializers()['title']
    grade = getGrade(source='*')
    class Meta: 
        model = StudentSubjectsScore
        fields = ['subjects','credit','score','grade']

class SubjectStudentScoreSerializers(serializers.ModelSerializer):
    class Meta:
        model = StudentSubjectsScore


class PersonnelSerializers(serializers.ModelSerializer):
    full_name = GetFullName(source='*') 

    class Meta:
        model = Personnel
        fields = ['id','full_name','school_class']

class PersonnelDetailSerializers(serializers.ModelSerializer):
    name = GetFullName(source='*')  
    role = getPersonnelType(source='*')
    title = getSchoolTitle(source='*')
    class_number = getClass(source='*')
    class Meta:
        model = Personnel
        fields = ['id','name','title','role','class_number']

class SchoolStructureSerializers(serializers.ModelSerializer):
    class Meta:
        model = SchoolStructure
        fields = ('__all__')