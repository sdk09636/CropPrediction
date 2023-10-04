# Importing Necessary Modules
import math
import numpy as np
import pickle
from flask import *
app = Flask(__name__)
1
norm_data = {'N': 140,
 'P': 145,
 'K': 205,
 'temperature': 43.67549305,
 'humidity': 99.98187601,
 'ph': 9.93509073,
 'rainfall': 298.5601175}

avg_val_dict = {'Apple': [0.1434285714285714, 0.9256551724137931, 0.9750731707317073, 0.5181395427887447, 0.9234673691336351, 0.5938546672940147, 0.37731094475470256], 
                'Banana': [0.7159285714285715, 0.5655862068965518, 0.24414634146341463, 0.626667224309675, 0.8036456526577231, 0.603920000637981, 0.3504151889945582], 
                'Blackgram': [0.28585714285714287, 0.4653103448275862, 0.09385365853658535, 0.6861971761987927, 0.6512180266900356, 0.7146386674216109, 0.22735789551663743], 
                'Chickpea': [0.28635714285714287, 0.4675172413793104, 0.3898536585365854, 0.43205007390294364, 0.1686305625863001, 0.7347693341095436, 0.2681202053050505], 
                'Coconut': [0.157, 0.11675862068965517, 0.14921951219512194, 0.627354108369934, 0.9485719190797569, 0.603920000637981, 0.5884242057213152], 
                'Coffee': [0.7228571428571429, 0.19820689655172413, 0.1460487804878049, 0.5847672966338728, 0.5887066971429196, 0.6844426673897118, 0.5294411099633896], 
                'Cotton': [0.8412142857142857, 0.31889655172413794, 0.09541463414634145, 0.5490493255004021, 0.7985447281666785, 0.6945080007336782, 0.26925900442814504], 
                'Grapes': [0.16557142857142856, 0.914, 0.9761463414634147, 0.5458438665525265, 0.8188484080035818, 0.603920000637981, 0.23315237340767728], 
                'Jute': [0.56, 0.32317241379310346, 0.19507317073170732, 0.5712585767821114, 0.7985447281666785, 0.6743773340457455, 0.5854432315461559], 
                'Kidneybeans': [0.14821428571428572, 0.4657931034482759, 0.09780487804878049, 0.4604412817269844, 0.21613917304210825, 0.573724000606082, 0.354769420935802], 
                'Lentil': [0.13407142857142856, 0.47144827586206894, 0.0946829268292683, 0.5611842772316454, 0.6481174647444986, 0.6945080007336782, 0.15300101159693574], 
                'Maize': [0.5554285714285715, 0.33406896551724136, 0.09653658536585366, 0.5124155089532526, 0.6510179904354848, 0.6240506673259137, 0.28389592256909535], 
                'Mango': [0.14335714285714285, 0.18744827586206897, 0.14595121951219514, 0.7145883840228336, 0.5015909082860587, 0.5837893339500483, 0.3171890498736825], 
                'Mothbeans': [0.15314285714285716, 0.3311034482758621, 0.0986829268292683, 0.645442055290089, 0.5316963645959497, 0.6844426673897118, 0.17145625620943827], 
                'Mungbean': [0.1499285714285714, 0.3260689655172414, 0.09692682926829269, 0.6529977799529386, 0.8550549700772713, 0.6743773340457455, 0.162111404581692], 
                'Muskmelon': [0.7165714285714285, 0.12220689655172413, 0.24429268292682926, 0.6562032389008142, 0.9235673872609105, 0.63411600066988, 0.08266341869992062], 
                'Orange': [0.13985714285714285, 0.11413793103448276, 0.04882926829268293, 0.5211160403832007, 0.921867079097229, 0.7045733340776446, 0.3700092327301553], 
                'Papaya': [0.3562857142857143, 0.4072413793103448, 0.24409756097560975, 0.7720576837311742, 0.9241674960245628, 0.6743773340457455, 0.47769273804629986], 
                'Pigeonpeas': [0.14807142857142858, 0.4671034482758621, 0.09897560975609755, 0.6351387943862032, 0.48068711968550315, 0.573724000606082, 0.5006026968756134], 
                'Pomegranate': [0.1347857142857143, 0.12931034482758622, 0.19614634146341464, 0.49982263451517, 0.9014133720694126, 0.6441813340138465, 0.36012847563271744], 
                'Rice': [0.5706428571428571, 0.32813793103448274, 0.19448780487804876, 0.5421804848978116, 0.8228491330945972, 0.6441813340138465, 0.7910634614484301], 
                'Watermelon': [0.7101428571428572, 0.11724137931034483, 0.24497560975609756, 0.5859121034009712, 0.8517543718771836, 0.6542466673578128, 0.17008299844335373]
               }


Label_mapping = {0: ['Apple', 'https://shorturl.at/cAO12'], 1: ['Banana', 'http://shorturl.at/pzEM1'], 2: ['Blackgram', 'http://shorturl.at/duFLR'], 
                 3: ['Chickpea', 'https://shorturl.at/cfkrG'], 
                 4: ['Coconut', 'http://shorturl.at/bmrOY'], 5: ['Coffee', 'http://shorturl.at/bxFHQ'], 6: ['Cotton', 'http://shorturl.at/lwIPZ'], 
                 7: ['Grapes', 'http://shorturl.at/bqKS8'], 8: ['Jute', 'http://shorturl.at/abfzK'], 
                 9: ['Kidneybeans', 'http://shorturl.at/aouRY'], 10: ['Lentil', 'http://shorturl.at/mxL36'], 
                 11: ['Maize', 'https://shorturl.at/mpBZ4'], 12: ['Mango', 'https://shorturl.at/kxDE0'], 13: ['Mothbeans', 'https://shorturl.at/mwOQ0'], 
                 14: ['Mungbean', 'https://shorturl.at/bACY2'], 15: ['Muskmelon', 'https://shorturl.at/oJX26'], 16: ['Orange', 'https://shorturl.at/iCEOX'], 
                 17: ['Papaya', 'https://shorturl.at/xD189'], 18: ['Pigeonpeas', 'https://shorturl.at/bvNXZ'], 
                 19: ['Pomegranate', 'http://shorturl.at/syIJ8'], 20: ['Rice', 'https://shorturl.at/ajoCD'], 21: ['Watermelon', 'http://shorturl.at/aiuDG']}

def std_div(arr,arr_mean):
    deviation_sum = 0
    
    for i in range(7):
        deviation_sum += (arr[i] - arr_mean[i]) ** 2
    ssd = math.sqrt((deviation_sum)/6)
    return ssd

def ValuePredictor(arr):
    #arr = [0.271429, 0.262069, 0.087805, 0.602409, 0.611986, 0.633525, 0.119688]
    to_predict = np.array(arr).reshape(1,-1)
    loaded_model = pickle.load(open("Crop_Prediction_Model.pkl", "rb"))
    result = loaded_model.predict(to_predict)
    return result[0]

def norm(x):
    #print(norm_data.keys())
    key = list(norm_data.keys())
    x_norm = x
    n = len(x)
    for i in range(n):
        x_norm[i] = x[i] / norm_data[key[i]]
    return np.array(x_norm)


@app.route('/')
def input():
    arr = [40, 72, 77, 17.02, 16.988, 7.486, 88.55]
    arr1 = [40, 72, 77, 17.02, 16.988, 7.486, 88.55]
    a = ValuePredictor(norm(arr))
    return render_template('a.html', arr = arr1, result = Label_mapping[a][0], link1 = Label_mapping[a][1])

@app.route('/', methods=['POST'])
def display():
    if request.method == 'POST':
        temp = request.form
        N = float(request.form.get('n'))
        P = float(request.form.get('p'))
        K = float(request.form.get('k'))
        temp = float(request.form.get('temp'))
        hum = float(request.form.get('hum'))
        ph = float(request.form.get('ph'))
        rf = float(request.form.get('rf'))
        arr = [N, P, K, temp, hum, ph, rf]
        #app.logger.info('%s', arr[3])
        app.logger.info('Hiiii')
        a = ValuePredictor(norm(arr))
        name = Label_mapping[a][0]
        arr_mean = avg_val_dict[name]
        sd = std_div(arr, arr_mean)
        app.logger.info(sd)
        if (sd < 0.2):
            return render_template('a.html',arr = [N, P, K, temp, hum, ph, rf], result = Label_mapping[a][0], link1 = Label_mapping[a][1])
        else:
            return render_template('a.html',arr = [N, P, K, temp, hum, ph, rf], result = 'The crops in this dataset are not suitable for given soil type.', link1 = 'https://shorturl.at/fGIJR')


if __name__ == '__main__':
    app.run(debug=True)