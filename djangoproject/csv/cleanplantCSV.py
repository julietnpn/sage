import csv
from ast import literal_eval
import urllib
import urlparse
import os

#1st layer cleaning (Repeating and blank url):
reader_1=csv.reader(open('Twitter_Original_Common.csv', 'r'), delimiter=',')
writer_1=csv.writer(open('Twitter_Cleaned_Common.csv', 'w'), delimiter=',',lineterminator = '\n')

entries = set()
normal_context = ""
tags_filter_nospace = []
hashtag = []
related_intersec = []
unrelated_intersec = []
tag_entries = set()
count =0
tag_list = []
normal_content = ""


tags_filter_related = ["feed", "ca", "native", "flower", "flora", "tree", "green", "plant", "garden", "forage", "bloom",
                       "nature", "yard", "botanical", "succulent", "cactus", "gardening","annual", "biennial", "vineyard",
                       "perennial", "canopy", "understory", "shrub", "herb", "ground cover", "vine", "palm", "evergreen",
                       "deciduous", "timber", "greens", "companion", "beneficial", "nitrogen", "fixer", ""
                       "hummingbird", "bees", "polyculture", "farm", "urban farm", "forest"]

tags_filter_unrelated = ["spray","jewelry", "fruit", "egg", "breakfast", "dinner", "brunch", "lunch", "dining", "hair",
                         "pasta", "smoothie", "biscuit", "cake", "food", "wine", "salad", "wines", "burger",
                         "hotdog", "dish","fish","toast", "baseball", "recipt", "receipt", "starter", "outfit", "oil", "pork", "gym", "gel",
                         "music", "dress", "shoes", "store", "detox", "medicine", "products","cheeto", "cola",
                         "sourdought","halloumi", "wheat", "toast", "bacon", "chicken", "cheese", "cream", "fastfood",
                         "healthyeating", "hummus","steak","recipe", "juice", "admin", "makeup","paint", "beauty",
                         "grill", "grilled", "yummy", "cooking", "skin", "wrap", "salmon", "mask", "game",
                         "beauty", "skincare", "event", "dessert", "cocktail", "pie", "yogurt", "video",
                         "food", "vegan", "snack", "chip", "drink", "acai", "emoji","guacamole","spaghetti",
                         "healthyfat", "sushi","erp", "academy", "document", "keeper", "cooking", "baking",
                         "butter", "bread", "tempura", "taco", "rice", "candle","dip"
                         ]

#eliminate the space between each hashtag
for plant in tags_filter_related:
    tags_filter_nospace.append(plant.replace(" ",""))
tags_filter_related = tags_filter_nospace

tags_filter_nospace = []
for plant in tags_filter_unrelated:
    tags_filter_nospace.append(plant.replace(" ",""))
tags_filter_unrelated = tags_filter_nospace


with open(r"Twitter_Original_Common.csv") as f:
    reader = csv.reader(f, delimiter=',')
    #for each record
    for row in reader:
        if(count == 0 and row):
            header = row
            writer_1.writerow(header)
            count = 1
        else:
            url = row[4]
            normal_content = str(row[7]).lower()
            tag_string = str(row[5]).lower()
            if((url in entries)):
                continue
            else:
                entries.add(url)
                if(tag_string != '' and url != '' and normal_content != ''):
                    tag_list = eval(tag_string)
                    tag_set = set(tag_list)
                    unrelated_intersec = tag_set.intersection(tags_filter_unrelated)
                    related_intersec = tag_set.intersection(tags_filter_related)
                    # download the photo based on given label
                    #image = urllib.URLopener()
                    #image.retrieve(url, os.path.basename(urlparse.urlparse(url).path))

                    # if not any (x in normal_content for x in tags_filter_related):
                    #    count +=1
                    # else:
                    #     if not any(x in normal_content for x in tags_filter_unrelated):
                    #         writer_1.writerow(row)
                    #         print normal_content

                    #FOR TWITTER:
                    for x in tags_filter_related:
						if x in normal_content:
							print x
							print normal_content
							if any(x in normal_content for x in tags_filter_unrelated):
								continue
							else:
								writer_1.writerow(row)
								#print normal_content
                    #FOR FLICKR:
                    # if any(x in normal_content for x in tags_filter_unrelated):
                    #    continue
                    # else:
                    #   writer_1.writerow(row)
                    #    image = urllib.URLopener()
                     #   image.retrieve(url, os.path.basename(urlparse.urlparse(url).path))
                    #  print normal_content

                #-----Down to 5039
                # if any(x in normal_content for x in tags_filter_related):
                #     if any(x in normal_content for x in tags_filter_unrelated):
                #         count +=1
                #     else:
                #         print tag_set
                #         writer_1.writerow(row)

                # else:
                #     if any(x in normal_content for x in tags_filter_related):
                #         writer_1.writerow(row)
                #         print tag_set

                # if(bool(unrelated_intersec)==False):
                #     if any(x in normal_content for x in tags_filter_related):
                #        # print normal_content
                #         writer_1.writerow(row)
                #else:
                   #print tag_set


reader_2=csv.reader(open('Flickr_Cleaned_Scientific.csv', 'r'), delimiter=',')
row_count_1 = sum(1 for row in reader_1)
row_count_2 = sum(1 for row in reader_2)
print "before:" + str(row_count_1) + "after:" + str(row_count_2)

