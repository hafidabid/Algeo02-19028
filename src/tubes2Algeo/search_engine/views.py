from django.shortcuts import render,redirect
# Create your views here.
from django.http import HttpResponse
from django.conf.urls.static import static
from django.template.defaulttags import register
from .supporter import *
from .objekPendukung import *
from django.core.files.storage import FileSystemStorage
from search_engine.models import *
from django.conf import settings
import os
import shutil
import sweetify
def cobacek(request):
    a = filestorage.objects.all()
    listfile = []
    for x in a: 
        listfile.append(x.judul)
    
    return render(request,'searchbar.html',{'list' : listfile})

def perihal(request):
    a = filestorage.objects.all()
    listfile = []
    for x in a: 
        listfile.append(x.judul)
    return render(request,'perihal.html',{'list' : listfile})

def searchresult(req):
    if req.method=="GET":
        q = req.GET['pencarian']
        req.session['latest_query'] = q
        q = stemming(q)
        arrq = read_query(q)
        if "kamus_kata" in req.session.keys():
            oldkamus = req.session["kamus_kata"]
            oldkamus = appendKK(oldkamus,arrq)
            vektor_queri = toVector(hitungKamusKata(makeNolDict(oldkamus),arrq))

            allfile = filestorage.objects.all()
            vektor_dokumen = dict()
            preview_dokumen = dict()
            obj_docs = []
            medpath = os.path.join(settings.BASE_DIR,'media')
            cnt = 1
            for x in allfile:
                newpath = os.path.join(medpath,x.url_sastrawee)
                prevpath = os.path.join(medpath,x.url_dokumen)
                hasil = HasilPencarian(cnt,x.judul,prevpath,newpath)
                if os.path.exists(newpath):
                    arr = makeDocsVektor(makeNolDict(oldkamus),newpath)
                    vektor_dokumen[x.judul] = toVector(arr)
                    hasil.setvectorDict(arr)
                    hasil.setJumlahKata(len(read_doc(newpath)))
                
                if os.path.exists(prevpath):
                    preview_dokumen[x.judul] = getPrevDocs(prevpath)
                    hasil.setpreview(getPrevDocs(prevpath))
                
                obj_docs.append(hasil)
                cnt=cnt+1
            
            dotsim = dict()
            cnt =0
            for x in vektor_dokumen:
                dotsim[x] = sim(vektor_queri,vektor_dokumen[x])
                obj_docs[cnt].setsimilaritas(dotsim[x])
                cnt=cnt+1
            
            result_pencarian = sortDictionary(dotsim)

            #sorting untuk hasil pencarian
            obj_docs.sort(key=lambda x:x.similaritas ,reverse=True)

            return render(req,'qresult.html',{
                'result_pencarian' : obj_docs,
                'preview_dokumen' : preview_dokumen,
                'dict_query' : hitungKamusKata(makeNolDict(oldkamus),arrq)
        })

        else:
            sweetify.error(req,"tidak ada dokumen, tambahkan dokumen dulu bosq")
            return redirect('/')
        

def reset(request):
    a = filestorage.objects.all()
    for x in a: 
        x.delete()

    medpath = os.path.join(settings.BASE_DIR,'media')
    if os.path.exists(medpath):
        shutil.rmtree(medpath)
    
    request.session.flush()

    sweetify.success(request,"berhasil reset app semua kamus kata dan dokumen telah berhasil di hapus dan aplikasi berada pada posisi kosongan")
    return redirect('/')

def upfile(request):
    if(request.method=="POST"):
        fileku = request.FILES["upfile"]
        filename = fileku.name
        fileext = getFileExtension(filename)
        if(fileext!=".txt"):
            sweetify.error(request,"format file tidak di dukung maaf. kami hanya terima format txt saja")
            return redirect('/')
        else:
            fstorage = FileSystemStorage()
            flname = fstorage.save(name=ignoreSpace(filename),content=fileku)
            medpath = os.path.join(settings.BASE_DIR,'media')
            full_path=os.path.join(medpath,ignoreSpace(filename))
            sastrawee = stemming(txtToStr(full_path))
            sastawi_flname = getjudul(filename)+"stemmed.txt"
            sastawi_flname = ignoreSpace(sastawi_flname)
            f = open(os.path.join(medpath,sastawi_flname),'a')
            f.write(sastrawee)
            f.close()

            arr = read_query(sastrawee)
            if 'kamus_kata' not in request.session:
                request.session['kamus_kata'] = appendKK([],arr)
            else:
                oldarr = request.session['kamus_kata']
                request.session['kamus_kata'] = appendKK(oldarr,arr)

            pushdb = filestorage(url_dokumen=ignoreSpace(filename),url_sastrawee=sastawi_flname, judul=getjudul(filename))
            pushdb.save()
            #return HttpResponse("oke oce = "+fstorage.url(flname)+" <a href='/' >click here to return to homepage</a>")
            sweetify.success(request, 'Berhasil upload file', text='file! '+filename+' telah berhasil diupload ke server!')
            return redirect('/')
    
def artikel(request):
    my_param = request.GET.get('konten', "nAn")
    if my_param!="nAn":
        getdb = filestorage.objects.filter(judul=my_param).first()
        #print(getdb.url_sastrawee)
        medpath = os.path.join(settings.BASE_DIR,'media')
        newpath = os.path.join(medpath,getdb.url_dokumen)
        fi = open(newpath,'r')
        arroftxt = fi.readlines()

        if "latest_query" in request.session:
            lat_q = "/q/?pencarian="+request.session['latest_query']
        else:
            lat_q = "/"
        
        print(arroftxt)
        return render(request,'tampilanartikel.html',{
            'judul': getdb.judul,
            'artikel' : arroftxt,
            'backtrace' : lat_q,
        })
    else:
        return HttpResponse("an error was happened, <a href='/' >click here to return to homepage</a>")



@register.filter
def get_item(dictionary, key):
    return dictionary[key]