from django.shortcuts import render
from django.conf import settings
import os
import random
import json
# Create your views here.
def index(request):

    if request.method == 'POST':
        file_path = os.path.join(settings.DATAS_DIR, "wordmaster.csv") 
        f = open(file_path, 'r', encoding = 'utf-8')
        try:
            startday = "unit"+request.POST['start']
            endday = "unit"+request.POST['end']
            vocanum = int(request.POST['voca']) + 1
        except: 
            startday = 1
            endday = 10
            vocanum = 50
            
        entire_voca_list=[] #시험범위의 모든 단어

        while True:  
            line = f.readline()
            line = line[:-1]
            if startday in line: 
                while(1):
                    nline = f.readline()
                    nline = nline[:-1]
                    if "unit" not in nline:
                        entire_voca_list.append(nline)
                    if endday in nline:
                        while(1):
                            nline = f.readline()                    
                            if "unit" in nline:
                                break
                            nline = nline[:-1]
                            entire_voca_list.append(nline)
                        break
                break

            if not line: break

        f.close()

        testvocalist = {} #최종 시험 단어
        used_idx = []
        total_size = len(entire_voca_list)
        for i in range(1,vocanum):
            num = 0
            while(True):
                num = random.randrange(0,total_size-1)
                if num not in used_idx:
                    break
            used_idx.append(num)
            voca = entire_voca_list[num].split(",")
            vocamean = voca[1].replace("\"", "")
            vocamean = vocamean.replace("|", ",")
            testvocalist[voca[0]] = vocamean
        context = {
            'testlist' : testvocalist, 
        }
        return render(request, 'voca/Word-Test-Generator.html', context)


    else:
        context = {
        }
        return render(request, 'voca/Word-Test-Generator.html')