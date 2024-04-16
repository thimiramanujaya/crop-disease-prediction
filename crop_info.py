# Define remedies and consequences for each disease

disease_info = {

    'rice': {
        'Rice__Bacterialblight': {
            'consequences': ['Yield loss', 'Reduced grain quality', 'Spread to new areas'],
            'remedies': ['Resistant Varieties', 'Copper-Based Bactericides', 'Practice crop rotation, weed removal, Nitrogen management)']   
        },
        'Rice__Blast': {
            'consequences': ['Significant Yield Loss', 'Damaged Grains', 'Increased Vulnerability to Other Diseases'],
            'remedies': ['Planting Resistant Varieties', 'Fungicide Application', 'Improved Field Sanitation']      
        },
        'Rice__Brownspot': {
            'consequences': ['Yield Loss', 'Poor Grain Quality', 'Spread Through Wind and Water'],
            'remedies': ['Resistant Rice Varieties', 'Copper Fungicides', 'Practice crop rotation, weed removal)']       
        },
        'Rice__Healthy': {
            'consequences': ['No specific consequences'],
            'remedies': ['Maintain good crop management practices']       
        },
        'class_name': ['Rice__Bacterialblight', 'Rice__Blast', 'Rice__Brownspot', 'Rice__Healthy'],
    },

    'potato': {
        'Potato__Early_Blight': {
            'consequences': ['Reduces potato yield', 'Affects quality of potatoes'],
            'remedies': ['Apply fungicide', 'Remove infected leaves', 'Improve air circulation']   
        },
        'Potato__Late_Blight': {
            'consequences': ['Significant reduction in potato yield', 'Loss of crop'],
            'remedies': ['Apply fungicide', 'Remove infected leaves', 'Practice crop rotation']      
        },
        'Potato__Healthy': {
            'consequences': ['No specific consequences'],
            'remedies': ['Maintain good crop management practices']       
        },
        'class_name': ['Potato__Early_Blight', 'Potato__Late_Blight', 'Potato__Healthy'],
    },

    'tomato': {
        'Tomato_Bacterial_spot': {
            'consequences': ['Reduced Yield', 'Fruit Scarring and Blemishes', 'Spread During Rain and Irrigation'],
            'remedies': ['Planting Resistant Tomato Varieties', 'Copper-Based Sprays', 'Clean Tools', 'Remove Infected Plants)']   
        },
        'Tomato__Early_Blight': {
            'consequences': ['Leaf Loss', 'Sunburn on Exposed Fruit', 'Reduced Fruit Quality and Yield'],
            'remedies': ['Resistant Tomato Varieties', 'Fungicide Sprays', 'Practice Spacing & Watering Practices)']   
        },
        'Tomato__Late_Blight': {
            'consequences': ['Devastating Yield Loss', 'Inedible Fruits', 'Rapid Spread'],
            'remedies': ['Resistant Tomato Varieties', 'Copper-Based Fungicides', 'Practices Spacing, Watering at Base, Crop Rotation, Sanitation, Staking']      
        },
        'Tomato_Leaf_Mold': {
            'consequences': ['Reduced Yield', 'Poor Fruit Quality', 'Spread in Humid Conditions'],
            'remedies': ['Improved Airflow', 'Apply Fungicides', 'Resistant Tomato Varieties']      
        },
        'Tomato_Septoria_leaf_spot': {
            'consequences': ['Leaf Loss', 'Reduced Photosynthesis', 'Potential Fruit Sunburn'],
            'remedies': ['Spacing', 'Sanitation', 'Apply Copper-Based Fungicides', 'Resistant Tomato Varieties']      
        },
        'Tomato_Spider_mites_Two_spotted_spider_mite': {
            'consequences': ['Yellowing', 'Stunted Growth', 'Fruit Bronzing and Scarring', 'Spread During Dry, Hot Weather'],
            'remedies': ['Insecticidal Soap Sprays', 'Predatory Mites', 'Water Management']      
        },
        'Tomato__Target_Spot': {
            'consequences': ['Reduced Yield', 'Fruit Blemishes', 'Weakened Plants'],
            'remedies': ['Resistant Varieties', 'Practice Crop Rotation, Spacing, Watering at Base, & Sanitation']      
        },
        'Tomato__Tomato_YellowLeaf__Curl_Virus': {
            'consequences': ['Stunted Growth', 'Yellowing and Curling of Leaves', 'Reduced Fruit Production'],
            'remedies': ['Planting Virus-Resistant Varieties', 'Manage Whiteflies that Transmit Virus', 'Removing Infected Plants']      
        },
        'Tomato__mosaic_virus': {
            'consequences': [ 'Discolored Patches', 'Deformed or Stunted Fruit', 'Reduced Plant Vigor'],
            'remedies': ['Resistant Tomato Varieties', 'Weed Control', 'Manage Aphids that Transmit Virus)']      
        },
        'Tomato__Healthy': {
            'consequences': ['No specific consequences'],
            'remedies': ['Maintain good crop management practices']       
        },
        'class_name': ['Tomato_Bacterial_spot', 'Tomato__Early_Blight', 'Tomato__Late_Blight', 'Tomato_Leaf_Mold', 
                       'Tomato_Septoria_leaf_spot', 'Tomato_Spider_mites_Two_spotted_spider_mite', 'Tomato__Target_Spot',
                       'Tomato__Tomato_YellowLeaf__Curl_Virus', 'Tomato__mosaic_virus', 'Tomato__Healthy']

    },

    'bellpepper': {
        'Pepper__bell___Bacterial_spot': {
            'consequences': ['Reduced Yield', 'Poor Fruit Quality', 'Spread in Humid Weather'],
            'remedies': ['Copper Sprays', 'Practice Spacing, Watering at Base, Crop Rotation, Sanitation, Tool Disinfection', 'Resistant Varieties']   
        },
        'Pepper__bell___healthy': {
            'consequences': ['No specific consequences'],
            'remedies': ['Maintain good crop management practices']       
        },
        'class_name': ['Pepper__bell___Bacterial_spot', 'Pepper__bell___healthy']
    },

    'coconut': {
        'CCI_Caterpillars': {
            'consequences': ['Reduced Yield', 'Decreased Nut Quality', 'Spread Potential'],
            'remedies': ['Biological Control', 'Cultural Practices', 'Pheromone Traps', 'Insecticides']   
        },
        'CCI_Leaflets': {
            'consequences': ['Yield Loss', 'Weakened Trees', 'Increased Disease Susceptibility', 'Poor Fruit Quality'],
            'remedies': ['Apply Fungicide', 'Improved Sanitation Practices', 'Nutrient Management', 'Resistant Variety Selection']   
        },
        'WCLWD_DryingofLeaflets': {
            'consequences': [ 'Reduced Photosynthesis', 'Premature Leaf Drop', 'Yield Decline', 'Weakened Trees'],
            'remedies': ['Improve Drainage', 'Nutrient Management', 'Apply copper-based fungicides with caution', 'Disease Resistance Management']   
        },
        'WCLWD_Flaccidity': {
            'consequences': ['Reduced Growth', 'Leaf Yellowing and Wilting (Flaccidity)', 'Premature Nut Drop', 'Yield Decline', 'Tree Death (in severe cases)'],
            'remedies': ['Maintain good agricultural practices: proper drainage, fertilization, and sanitation', 'Removing and destroying severely affected palms', 'Ensure optimal nutrient balance']   
        },
        'WCLWD_Yellowing': {
            'consequences': ['Significant Yield Loss', 'Tree Death', 'Reduced Fruit Quality', 'Economic Impact'],
            'remedies': ['Planting Resistant Varieties', 'Insect Vector Control', 'Quarantine Measures', 'Early Detection']   
        },
        'class_name': ['CCI_Caterpillars', 'CCI_Leaflets', 'WCLWD_DryingofLeaflets', 'WCLWD_Flaccidity', 'WCLWD_Yellowing'],

    },

    'cinnamon': {
        'leaf_spot_disease': {
            'consequences': ['Reduced Yield', 'Decreased Cinnamon Quality', 'Spread in Humid Conditions'],
            'remedies': ['Apply Copper or Chlorothalonil Fungicides Cautiously', 'Practice Pruning, Watering at Base, Removing Infected Leaves, Crop Rotation', 'Resistant Varieties']   
        },
        'healthy_leaves': {
            'consequences': ['No specific consequences'],
            'remedies': ['Maintain good crop management practices']       
        },
        'class_name': ['leaf_spot_disease', 'healthy_leaves']

    },

}

image_sizes = {
    'rice': 256,
    'potato': 256,
    'tomato': 256,
    'bellpepper': 256,
    'coconut': 256,
}