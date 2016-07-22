
from plants.models import Human_Needs_Library, PlantFoodProd, Chosen_Plants, Chosen_Human_Needs, Plant, PlantMedicinalsProd, PlantCulturalAndAmenityProd, PlantBiochemicalMaterialProd, PlantRawMaterialsProd, PlantMineralNutrientsProd
from django import forms

class Human_Needs (forms.Form):



   #     for choice in Human_Needs_Library:
   #         self.fields.append(forms.BooleanField(required=False, label=choice.need, initial= choice.type))

    print 'TEST'
    sortedobj = Human_Needs_Library.objects.order_by('id')
    list = []

    for i in range(0, len(sortedobj), 1):
        newTuple = (str(sortedobj[i].id), sortedobj[i].need)
        list.append(newTuple)
        #(forms.BooleanField(required=False, label=sortedobj[i].need, initial=sortedobj[i].type))

    #print sortedobj, list

    class Meta:
        model = Human_Needs_Library

        def __str__(self):
            return self.need


    picked = forms.MultipleChoiceField(choices=list, required=False, widget=forms.CheckboxSelectMultiple())




class Plants (forms.Form):
    plantChoiceList = []
    plantrecLabel = "Here are the plant recommendations"
    plantrec = forms.MultipleChoiceField(label= plantrecLabel, required= False, widget= forms.CheckboxSelectMultiple())
    #plantrec = forms.MultipleChoiceField(label=plantrecLabel, required=False, choices= plantChoiceList,widget=forms.CheckboxSelectMultiple())
    #@classmethod
    def __init__(self, *args, **kwargs):

        # Task 1: List all of the choices
        # Get ID of each choice form Chosen_Human_Needs
        blank = [(), ()]
        idList = []
        choiceList = []
        entireList = ""
        chosenItems = Chosen_Human_Needs.objects.order_by('id')
        humanNeeds = Human_Needs_Library.objects.order_by('id')
        foodTable = PlantFoodProd.objects.order_by('id')
        medicineTable = PlantMedicinalsProd.objects.order_by('id')
        cultureTable = PlantCulturalAndAmenityProd.objects.order_by('id')
        biochemTable = PlantBiochemicalMaterialProd.objects.order_by('id')
        mineralTable = PlantMineralNutrientsProd.objects.order_by('id')
        rawmaterialsTable = PlantRawMaterialsProd.objects.order_by('id')

        allPlantsTable = Plant.objects.order_by('id')

        print chosenItems[0].human_need_lib_id

        # for i in range(0, len(chosenItems), 1):
        # idList.append(chosenItems[i].human_need_lib_id)

        #super(Plants, self).__init__(*args, **kwargs)
        # Convert ID to text from Human_Needs_Library
        for i in range(0, len(chosenItems), 1):
            for j in range(0, len(humanNeeds), 1):
                if (chosenItems[i].human_need_lib_id == humanNeeds[j].id):
                    choiceList.append(humanNeeds[j].need)
                    entireList = entireList + humanNeeds[j].need + ", "
                    # choice = choice + humanNeeds[j].need
        entireList = entireList[:-2]
        #self.fields.update(forms.MultipleChoiceField(label=entireList, choices=blank, required=False, widget=forms.CheckboxSelectMultiple()))

        # Task 2: Convert choices to actual plants and categorize them
        # create array with all plant IDs
        PlantIds = []  # IDs of all recommended plants
        for i in range(0, len(chosenItems), 1):
            if (chosenItems[i].human_need_lib_id == 1):  # Food
                for j in range(0, len(foodTable), 1):
                    PlantIds.append(foodTable[j].plants_id)

            if (chosenItems[i].human_need_lib_id == 3):  # medicine
                for j in range(0, len(medicineTable), 1):
                    PlantIds.append(medicineTable[j].plants_id)

            if (chosenItems[i].human_need_lib_id == 4):  # timber / other construction materials
                for j in range(0, len(rawmaterialsTable), 1):
                    if (rawmaterialsTable[j].raw_materials_prod_id >= 2 and rawmaterialsTable[
                        j].raw_materials_prod_id <= 10):
                        PlantIds.append(rawmaterialsTable[j].plants_id)

            if (chosenItems[i].human_need_lib_id == 5):  # raw products for household products
                for j in range(0, len(rawmaterialsTable), 1):
                    if (rawmaterialsTable[j].raw_materials_prod_id == 1 or rawmaterialsTable[
                        j].raw_materials_prod_id == 4 or rawmaterialsTable[j].raw_materials_prod_id == 8 or
                                rawmaterialsTable[j].raw_materials_prod_id == 12 or rawmaterialsTable[
                        j].raw_materials_prod_id == 11):
                        PlantIds.append(rawmaterialsTable[j].plants_id)
                for j in range(0, len(biochemTable), 1):
                    PlantIds.append(biochemTable[j].plants_id)

            if (chosenItems[i].human_need_lib_id == 6):  # flowers
                for j in range(0, len(cultureTable), 1):
                    if (cultureTable[j].cultural_and_amenity_prod_id == 1 or cultureTable[
                        j].cultural_and_amenity_prod_id == 3):
                        PlantIds.append(cultureTable[j].plants_id)

            if (chosenItems[i].human_need_lib_id == 7):  # fragrance
                for j in range(0, len(rawmaterialsTable), 1):
                    if (rawmaterialsTable[j].raw_materials_prod_id == 12):
                        PlantIds.append(rawmaterialsTable[j].plants_id)

            if (chosenItems[i].human_need_lib_id == 8):  # religious, spiritual, and cultural amenity
                for j in range(0, len(cultureTable), 1):
                    if (cultureTable[j].cultural_and_amenity_prod_id == 4 or cultureTable[
                        j].cultural_and_amenity_prod_id == 5):
                        PlantIds.append(cultureTable[j].plants_id)

            if (chosenItems[i].human_need_lib_id == 9):  # recreation
                for j in range(0, len(cultureTable), 1):
                    if (cultureTable[j].cultural_and_amenity_prod_id == 2):
                        PlantIds.append(cultureTable[j].plants_id)
        # print PlantIds
        # Deletes repeated IDs
        for i in range(len(PlantIds) - 1, -1, -1):
            for j in range(len(PlantIds) - 1, 0, -1):
                j = i - 1
                if (PlantIds[i] == PlantIds[j]):
                    PlantIds.remove(PlantIds[i])
                    break
        # print PlantIds

        # ID to actual name
        PlantNames = []
        for i in range(0, len(PlantIds), 1):
            for j in range(0, len(allPlantsTable), 1):
                if (PlantIds[i] == allPlantsTable[j].id):
                    PlantNames.append(allPlantsTable[j].common_name)

        # convert to tuple
        super(Plants, self).__init__(*args, **kwargs)
        plantrecLabel = "Here are the plant recommendations"
        plantChoiceList = []
        for i in range(len(self.plantChoiceList)-1, -1, -1):
            self.plantChoiceList.pop(i)


        for i in range(0, len(PlantNames), 1):
            newTuple = (str(PlantIds[i]), PlantNames[i])
            self.plantChoiceList.append(newTuple)
            #self.fields['plantrec'].choices.append(newTuple)
        self.fields['plantrec'].choices = self.plantChoiceList
        #print self.plantChoiceList

        #self.fields['plantrec'].widget = forms.CheckboxSelectMultiple()
        #self.fields['plantrec'].label.append(plantrecLabel)
        #print self.plantrec.choices
            #print self.fields['plantrec'].choices.append((str(PlantIds[i]), PlantNames[i]))


        #plantrec = self.fields.update(forms.MultipleChoiceField(label=plantrecLabel, choices=plantChoiceList, required=False,
                                         #widget=forms.CheckboxSelectMultiple()))


    # Task 3: Create checkboxes for each plant
    #def getPlantChoice(self):
     #   return self.plantChoiceList


        #self.fields.update(forms.MultipleChoiceField(label=plantrecLabel, choices=plantChoiceList, required=False,
          #                                   widget=forms.CheckboxSelectMultiple()))
        #return plantChoiceList


    #hi = self.plantChoiceList
    #object = Plants()

    #def __init__(self, *args, **kwargs):
      #  super(Plants, self).__init__(*args, **kwargs)



class Address (forms.Form):

    Address = forms.CharField(max_length=400)



