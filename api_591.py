from flask import Flask, request, jsonify, Response
import pymongo


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["web591_db"]
mycol = mydb["sites"]
app = Flask(__name__)

@app.route('/')
def index():
    return 'hello!!'

@app.route('/query/<string:phone_number>', methods=['GET'])
def query_db(phone_number):
    mydoc = mycol.find({'$and': [{'區域' : '新北'}, 
                                 {'性別要求' : '男女生皆可'},
                                 {'聯絡電話': phone_number}]
                        })
    json_list = []
    temp_dict = {}
    json_dict = {}
    index = 1
    # def generate():
    #     for i in mydoc:
    #         temp_dict = {'出租者' : str(i['出租者']),
    #                      '出租者身份' : str(i['出租者身份']),
    #                      '聯絡電話' : str(i['聯絡電話']),
    #                      '型態' : str(i['型態']),
    #                      '現況' : str(i['現況']),
    #                      '格局' : str(i['格局']),
    #                      '性別要求' : str(i['性別要求']),
    #                      '區域' : str(i['區域'])
    #                      }
    #         yield temp_dict + '\n'
    for i in mydoc:
        temp_dict = {'出租者' : str(i['出租者']),
                     '出租者身份' : str(i['出租者身份']),
                     '聯絡電話' : str(i['聯絡電話']),
                     '型態' : str(i['型態']),
                     '現況' : str(i['現況']),
                     '格局' : str(i['格局']),
                     '性別要求' : str(i['性別要求']),
                     '區域' : str(i['區域'])
                    }
        json_dict = {'id' : index, 'data' : temp_dict}
        index += 1
        json_list.append(json_dict)
    # return Response(generate(),  mimetype='application/json')
    return jsonify(releases=json_list)


if __name__ == '__main__':
    app.run(port=3000, debug=True)