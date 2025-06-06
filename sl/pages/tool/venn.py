import pandas as pd
import matplotlib.pyplot as plt


def venn_analysis(tab):
    
    count_testIsSubset = 0
    count_otherIsSubset = 0
    count_test_empty = 0
    count_other_empty = 0
    count_nothing = 0
    count_test_completed_by_other= 0
    count_other_completed_by_test = 0
    count_noIntersection = 0
    count_same = 0

    for index, row in tab.iterrows():  

        test = row[tab.columns[-2]]
        other = row[tab.columns[-1]]

        other = other.replace('|', '  ')

        other_set = set(other.split())
        test_set = set(test.split())


        if len(test_set) == 0 and len(other_set) == 0:
            count_nothing += 1
                
        elif len(test_set) == 0:
            count_test_empty += 1
                
        elif len(other_set) == 0:
            count_other_empty += 1      
            
        elif test_set == other_set:
            count_same += 1      
            
        else:
                 
            if test_set.issubset(other_set):
                count_testIsSubset += 1     

            elif other_set.issubset(test_set):
                count_otherIsSubset += 1
                    

            else:

                if len(test_set.intersection(other_set)) != 0:
                    if len(test_set) >= len(other_set):
                        count_other_completed_by_test += 1  
                     
                    elif len(other_set) > len(test_set):
                            count_test_completed_by_other += 1    
                    else:
                        count_noIntersection += 1
                       

    tot = count_testIsSubset + count_otherIsSubset + count_test_empty + count_other_empty + count_nothing  + count_noIntersection + count_test_completed_by_other + count_other_completed_by_test + count_same
    sous_tot = count_testIsSubset + count_same+count_otherIsSubset + count_test_completed_by_other + count_other_completed_by_test+count_noIntersection

        
    labels = [
            "Subset = Test",
            "Subset = InterPro",
            "Nothing in common",
            "Similar",
            "Intersection"
        ]

    values = [
            count_testIsSubset,
            count_otherIsSubset,
            count_noIntersection,
            count_same,
            count_test_completed_by_other + count_other_completed_by_test
        ]

    
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
    ax.set_title(f"Résulat comparatif de Test et de InterPro (non vide)" + str(tab.columns[-2]) + " sur " + str(sous_tot) + " clusters")
    ax.legend(labels, bbox_to_anchor=(1.09, 0), loc="lower right", fontsize="small", title="Categories")
    plt.close(fig)

    result_list = [
        "#####################################################################",
        "Processing completed.",
        "#####################################################################",
        f"Number of Test is susbset of {tab.columns[-1]}: {count_testIsSubset}",
        f"Number of {tab.columns[-1]} is subset of Test: {count_otherIsSubset}",
        f"Number of Test empty: {count_test_empty}",
        f"Number of {tab.columns[-1]} empty: {count_other_empty}",
        f"Number of nothing: {count_nothing}",
        f"Number of no intersection: {count_noIntersection}",
        f"Number of Test completed by {tab.columns[-1]}: {count_test_completed_by_other}",
        f"Number of {tab.columns[-1]} completed by Test: {count_other_completed_by_test}",
        f"Number of same: {count_same}",
        "#####################################################################",
        "Résultat total :",
        f"Somme total des CK analysé {tot}",
        f"Somme total des CK analysé avec prédictions existantes {sous_tot} soit : {round((sous_tot / tot * 100),2)} %",
        "#####################################################################"
    ]
    return fig, result_list