
from plants.models import Human_Needs_Library, PlantLayer, PlantFoodProd, Chosen_Plants, Chosen_Human_Needs, Plant, PlantMedicinalsProd, \
    PlantCulturalAndAmenityProd, PlantBiochemicalMaterialProd, PlantRawMaterialsProd, PlantMineralNutrientsProd, PlantNutrientRequirementsByRegion
from django import forms
from .models import ID_Table


UNIVERSALID = 1

class Human_Needs (forms.Form):



   #     for choice in Human_Needs_Library:
   #         self.fields.append(forms.BooleanField(required=False, label=choice.need, initial= choice.type))


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
    blank = []
    entireList = "The Human Needs you selected - "
    plantrecLabel = "Here are the plant recommendations"
    selectedchoices = forms.MultipleChoiceField(required= False, widget= forms.CheckboxSelectMultiple())
    plantrec = forms.MultipleChoiceField(label= plantrecLabel, required= False, widget= forms.CheckboxSelectMultiple())
    prefilteredplants = []

    #plantrec = forms.MultipleChoiceField(label=plantrecLabel, required=False, choices= plantChoiceList,widget=forms.CheckboxSelectMultiple())
    #@classmethod
    def __init__(self, *args, **kwargs):

        # Task 1: List all of the choices
        # Get ID of each choice form Chosen_Human_Needs
        idList = []
        choiceList = []
        #entireList = ""
        chosenItems = Chosen_Human_Needs.objects.order_by('id')
        humanNeeds = Human_Needs_Library.objects.order_by('id')
        foodTable = PlantFoodProd.objects.order_by('id')
        medicineTable = PlantMedicinalsProd.objects.order_by('id')
        cultureTable = PlantCulturalAndAmenityProd.objects.order_by('id')
        biochemTable = PlantBiochemicalMaterialProd.objects.order_by('id')
        mineralTable = PlantMineralNutrientsProd.objects.order_by('id')
        rawmaterialsTable = PlantRawMaterialsProd.objects.order_by('id')
        layerTable = PlantLayer.objects.order_by('id')

        allPlantsTable = Plant.objects.order_by('id')

        allIDs = ID_Table.objects.order_by('id')

        global UNIVERSALID

        #self.prefilteredplants = []

        #print chosenItems[0].human_need_lib_id

        # for i in range(0, len(chosenItems), 1):
        # idList.append(chosenItems[i].human_need_lib_id)

        #super(Plants, self).__init__(*args, **kwargs)
        # Convert ID to text from Human_Needs_Library
        for i in range(0, len(chosenItems), 1):
            for j in range(0, len(humanNeeds), 1):
                if (chosenItems[i].human_need_lib_id == humanNeeds[j].id and chosenItems[i].project_id == UNIVERSALID):
                    choiceList.append(humanNeeds[j].need)
                    self.entireList = self.entireList + humanNeeds[j].need + ", "
                    # choice = choice + humanNeeds[j].need
        self.entireList = self.entireList[:-2]

        #self.fields.update(forms.MultipleChoiceField(label=entireList, choices=blank, required=False, widget=forms.CheckboxSelectMultiple()))

        # Task 2: Convert choices to actual plants and categorize them
        # create array with all plant IDs
        PlantIds = []  # IDs of all recommended plants
        for i in range(0, len(chosenItems), 1):
            if (chosenItems[i].human_need_lib_id == 1 and chosenItems[i].project_id == UNIVERSALID):  # Food
                for j in range(0, len(foodTable), 1):
                    PlantIds.append(foodTable[j].plants_id)

            if (chosenItems[i].human_need_lib_id == 3 and chosenItems[i].project_id == UNIVERSALID):  # medicine
                for j in range(0, len(medicineTable), 1):
                    PlantIds.append(medicineTable[j].plants_id)

            if (chosenItems[i].human_need_lib_id == 4 and chosenItems[i].project_id == UNIVERSALID):  # timber / other construction materials
                for j in range(0, len(rawmaterialsTable), 1):
                    if (rawmaterialsTable[j].raw_materials_prod_id >= 2 and rawmaterialsTable[
                        j].raw_materials_prod_id <= 10):
                        PlantIds.append(rawmaterialsTable[j].plants_id)

            if (chosenItems[i].human_need_lib_id == 5 and chosenItems[i].project_id == UNIVERSALID):  # raw products for household products
                for j in range(0, len(rawmaterialsTable), 1):
                    if (rawmaterialsTable[j].raw_materials_prod_id == 1 or rawmaterialsTable[
                        j].raw_materials_prod_id == 4 or rawmaterialsTable[j].raw_materials_prod_id == 8 or
                                rawmaterialsTable[j].raw_materials_prod_id == 12 or rawmaterialsTable[
                        j].raw_materials_prod_id == 11):
                        PlantIds.append(rawmaterialsTable[j].plants_id)
                for j in range(0, len(biochemTable), 1):
                    PlantIds.append(biochemTable[j].plants_id)

            if (chosenItems[i].human_need_lib_id == 6 and chosenItems[i].project_id == UNIVERSALID):  # flowers
                for j in range(0, len(cultureTable), 1):
                    if (cultureTable[j].cultural_and_amenity_prod_id == 1 or cultureTable[
                        j].cultural_and_amenity_prod_id == 3):
                        PlantIds.append(cultureTable[j].plants_id)

            if (chosenItems[i].human_need_lib_id == 7 and chosenItems[i].project_id == UNIVERSALID):  # fragrance
                for j in range(0, len(rawmaterialsTable), 1):
                    if (rawmaterialsTable[j].raw_materials_prod_id == 12):
                        PlantIds.append(rawmaterialsTable[j].plants_id)

            if (chosenItems[i].human_need_lib_id == 8 and chosenItems[i].project_id == UNIVERSALID):  # religious, spiritual, and cultural amenity
                for j in range(0, len(cultureTable), 1):
                    if (cultureTable[j].cultural_and_amenity_prod_id == 4 or cultureTable[
                        j].cultural_and_amenity_prod_id == 5):
                        PlantIds.append(cultureTable[j].plants_id)

            if (chosenItems[i].human_need_lib_id == 9 and chosenItems[i].project_id == UNIVERSALID):  # recreation
                for j in range(0, len(cultureTable), 1):
                    if (cultureTable[j].cultural_and_amenity_prod_id == 2):
                        PlantIds.append(cultureTable[j].plants_id)

        # Deletes repeated IDs
        for i in range(len(PlantIds) - 1, -1, -1):
            for j in range(len(PlantIds) - 1, 0, -1):
                j = i - 1
                if (PlantIds[i] == PlantIds[j]):
                    PlantIds.remove(PlantIds[i])
                    break

        #self.prefilteredplants = PlantIds #Take plant IDs before they are filtered out by type

        #Find plants that are trees
        #ID for trees: 1, 2, 7, 8
        for i in range(len(self.prefilteredplants) - 1, -1, -1):
            self.prefilteredplants.pop(i)

        for i in range(len(PlantIds)-1, -1, -1):
            for j in range(len(layerTable)-1, -1, -1):
                if(PlantIds[i] == layerTable[j].plants_id):
                    if(layerTable[j].layer_id != 1 and layerTable[j].layer_id != 2 and layerTable[j].layer_id != 7 and layerTable[j].layer_id != 8):
                        self.prefilteredplants.append(PlantIds[i])
                        PlantIds.remove(PlantIds[i])
                        break




        # ID to actual name
        PlantNames = []
        for i in range(0, len(PlantIds), 1):
            for j in range(0, len(allPlantsTable), 1):
                if (PlantIds[i] == allPlantsTable[j].id):
                    PlantNames.append(allPlantsTable[j].common_name)

        # convert to tuple
        super(Plants, self).__init__(*args, **kwargs)

        for i in range(len(self.plantChoiceList)-1, -1, -1):
            self.plantChoiceList.pop(i)


        for i in range(0, len(PlantNames), 1):
            newTuple = (str(PlantIds[i]), PlantNames[i])
            self.plantChoiceList.append(newTuple)
            #self.fields['plantrec'].choices.append(newTuple)
        self.fields['plantrec'].choices = self.plantChoiceList
        self.fields['selectedchoices'].label = self.entireList


    def returnPlantIDs(self):
        return self.prefilteredplants
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

class Support (forms.Form):
    plantChoiceList = []
     #might put this inside
    blank = []
    plantobj = Plants()
    humanneedsList = "The Human Needs you selected - "
    chosenplantsList = "The Key Species you selected - "
    supportLabel = "Suggested support species"
    selectedchoices = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple())
    plantrec = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple())
    supportchoices = forms.MultipleChoiceField(label= supportLabel, required=False, widget=forms.CheckboxSelectMultiple())

    def __init__(self,*args, **kwargs):
        super(Support, self).__init__(*args, **kwargs)
        chosenItems = Chosen_Human_Needs.objects.order_by('id')
        humanNeeds = Human_Needs_Library.objects.order_by('id')
        chosenPlants = Chosen_Plants.objects.order_by('id')
        fertNeeds = PlantNutrientRequirementsByRegion.objects.order_by('id')
        chosenSupportID = []

        allPlantsTable = Plant.objects.order_by('id')
        allIDs = ID_Table.objects.order_by('id')

        global UNIVERSALID

        # Convert ID to text from Human_Needs_Library
        for i in range(0, len(chosenItems), 1):
            for j in range(0, len(humanNeeds), 1):
                if (chosenItems[i].human_need_lib_id == humanNeeds[j].id and chosenItems[i].project_id == UNIVERSALID):
                    #choiceList.append(humanNeeds[j].need)
                    self.humanneedsList = self.humanneedsList + humanNeeds[j].need + ", "
                    # choice = choice + humanNeeds[j].need
        self.humanneedsList = self.humanneedsList[:-2]

        for i in range(0, len(chosenPlants), 1):
            for j in range(0, len(allPlantsTable), 1):
                if (chosenPlants[i].plant_id == allPlantsTable[j].id and chosenPlants[i].project_id == UNIVERSALID):
                    self.chosenplantsList = self.chosenplantsList + allPlantsTable[j].common_name + ", "

        self.chosenplantsList = self.chosenplantsList[:-2]


        #Step 1: Gather all plants that are recommended based on human needs

        allPlants = self.plantobj.returnPlantIDs()
        print len(allPlants)


        #Step 2: Filter out recommended plants based on fertility value

        #Create list with fertIDs of key species
        keyfertID = []
        for i in range(0, len(chosenPlants), 1):
            for j in range(0, len(fertNeeds), 1):
                if (chosenPlants[i].plant_id == fertNeeds[j].plants_id and chosenPlants[i].project_id == UNIVERSALID):
                    keyfertID.append(fertNeeds[j].fertility_needs_id)
        #print keyfertID

        print len(chosenSupportID)
        for i in range(0, len(allPlants), 1):
            for j in range(0, len(fertNeeds), 1):
                #print "inside outer loop"
                if (allPlants[i] == fertNeeds[j].plants_id):
                    #print "inside if"
                    for k in range(0, len(keyfertID), 1):
                        #print "inside loop"
                        if (fertNeeds[j].fertility_needs_id == keyfertID[k]):
                            chosenSupportID.append(allPlants[i])
                            #print "adding ID"
                            break
                            break
                elif (allPlants[i] > 33160):
                    chosenSupportID.append(allPlants[i])
                    break
        #print self.chosenSupportID

        PlantNames = []
        for i in range(0, len(chosenSupportID), 1):
            for j in range(0, len(allPlantsTable), 1):
                if (chosenSupportID[i] == allPlantsTable[j].id):
                    PlantNames.append(allPlantsTable[j].common_name)

        #for i in range(len(self.plantChoiceList) - 1, -1, -1):
            #self.plantChoiceList.pop(i)

        while len(self.plantChoiceList) > 0:
            self.plantChoiceList.pop(0)
        print len(self.plantChoiceList)

        for i in range(0, len(PlantNames), 1):
            newTuple = (str(chosenSupportID[i]), PlantNames[i])
            self.plantChoiceList.append(newTuple)
        #print self.plantChoiceList

        print len(self.plantChoiceList)

        self.fields['supportchoices'].choices = self.plantChoiceList
        self.fields['selectedchoices'].label = self.humanneedsList
        self.fields['plantrec'].label = self.chosenplantsList


class Address (forms.Form):
    def __init__(self, *args, **kwargs):
        allIDs = ID_Table.objects.order_by('id')
        global UNIVERSALID
        UNIVERSALID = allIDs[0].id_Value
        print UNIVERSALID

    Address = forms.CharField(max_length=400)



class IDForm (forms.Form):

    IDForm = forms.CharField(max_length=400)