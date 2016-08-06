from django.db import models

class Human_Needs_Library(models.Model):
    need = models.TextField()
    type = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'Human_Needs_Library'

    def __str__(self):
        return self.need

class SPC_Project(models.Model):
    user_id = models.IntegerField()
    address = models.TextField()
    polyculture_coordinates = models.TextField()

    class Meta:
        managed = True
        db_table = 'SPC_Project'

    def __str__(self):
        return self.address

class ID_Table(models.Model):
    id = models.IntegerField(primary_key= True)
    id_Value = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'ID_Table'


class Chosen_Human_Needs(models.Model):
    project_id = models.IntegerField()
    human_need_lib_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'Chosen_Human_Needs'

        # def __str__(self):
        #  return self.project_id


class Chosen_Plants(models.Model):
    project_id = models.IntegerField()
    plant_id = models.IntegerField()
    key_species = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'Chosen_Plants'

    def __str__(self):
        return self.plant_id
