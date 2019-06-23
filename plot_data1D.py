#!/usr/bin/env python

#Script to plot data, the data and the related config is loaded by a file passed to the script.
#The options for the config are read via argparse in the following:
#All options not specific for input file have to be in the first line of the file
#All files to plot, with their corresponding options have to written from the second line on, one file per line only
#Call with <python (-i) plot_data1D.py #CONFIG_FILE (-b)
#The option -i stops python from closing automatically instead it goes to prompt
#The option -b let python run in background

import sys
import ROOT
import uncertainties as unc
from uncertainties import unumpy
import numpy as np
import argparse 

def Read_Data( datafile ):
    
    Converters = dict.fromkeys(range(int(datafile[1])), unc.ufloat_fromstr)
    
    Value0 = np.array(unc.ufloat(0.,0.), dtype=object) #Adding underflow bin
    Values = np.loadtxt(datafile[0],converters=Converters, dtype=object)
    if config.tgrapherrors:
        FillValues = Values
    else:
        FillValues = np.hstack((Value0,Values))
    #print FillValues

    return FillValues

def Read_hep_data( datafile ):

    return Fillvalues

def Plot_Histo():
    print "Test Plot_Histo"

def Plot_Ratio():
    print "Test Plot_Ratio"


def Save_Plots():
    TCspectrum.SaveAs("plots/%s.pdf"%(config.name))
    TCspectrum.SaveAs("plots/%s.png"%(config.name))
    if config.ratio:
        TCratio.SaveAs("plots/%s_ratio.pdf"%(config.name))
        TCratio.SaveAs("plots/%s_ratio.png"%(config.name))
    if config.plusratio:
        TCplus.SaveAs("plots/%s_plus.pdf"%(config.name))
        TCplus.SaveAs("plots/%s_plus.png"%(config.name))





    

fileparser = argparse.ArgumentParser()
fileparser.add_argument("-f", "--filename")
fileparser.add_argument("-ld", "--legend", default="", nargs='+')
fileparser.add_argument("-nc", "--numbercolumns")
fileparser.add_argument("-nm", "--nomarker", action="store_true")
fileparser.add_argument("-rd", "--ratiodivisor", action="store_true") #Ratio can only be calculated with exactly one input variable chosen as divisor - only works if the same binning is chosen for all files
fileparser.add_argument("-rld", "--ratiolegend", default="", nargs='+')
fileparser.add_argument("-rnm", "--rationomarker", action="store_true")
fileparser.add_argument("-sr", "--skipratio", action="store_true")
fileparser.add_argument("-fb", "--filebinning")

parser = argparse.ArgumentParser()
parser.add_argument("-ac", "--alternativecolors", action="store_true")
parser.add_argument("-bc", "--bincenter") #This option will only work with tgrapherrors
parser.add_argument("-bm", "--bottommargin", default=0.1, type=float)
parser.add_argument("-fb", "--filebinning") #This binning is needed even if every file has it's own binning, it defines the size of the base histogram
parser.add_argument("-lb", "--label", nargs='+')
parser.add_argument("-lbx", "--labelbox", nargs=4, default=[0.15,0.25,0.6,0.15], type=float)
parser.add_argument("-lm", "--leftmargin", default=0.08, type=float)
parser.add_argument("-lp", "--legendposition", nargs =2, default=[0.5,0.8], type=float) #Defines top left corner of TLegend
parser.add_argument("-lt", "--legendtitle", nargs='+')
parser.add_argument("-ms", "--markersize", default=1., type=float)
parser.add_argument("-n", "--name", default="plot")
parser.add_argument("-rm", "--rightmargin", default=0.04, type=float)
parser.add_argument("-s", "--save", action="store_true")
parser.add_argument("-sx", "--sizex", default=1200, type=int)
parser.add_argument("-sy", "--sizey", default=900, type =int)
parser.add_argument("-t", "--title", default="")
parser.add_argument("-tge", "--tgrapherrors", action="store_true")
parser.add_argument("-tm", "--topmargin", default=0.04, type=float)
parser.add_argument("-tox", "--titleoffsetx", default=1., type=float)
parser.add_argument("-toy", "--titleoffsety", default=1., type=float)
parser.add_argument("-xr", "--xrange", nargs=2, type=float)
parser.add_argument("-xt", "--xtitle", default="", nargs='+')
parser.add_argument("-yr", "--yrange", nargs=2, type=float)
parser.add_argument("-yt", "--ytitle", default="", nargs='+')
parser.add_argument("--xlog", action="store_true")
parser.add_argument("--xrlog", action="store_true")
parser.add_argument("--ylog", action="store_true")
parser.add_argument("--yrlog", action="store_true")
parser.add_argument("-st", "--stack", action="store_true")
#ratio config
parser.add_argument("-mxl", "--morexlables", action="store_true")
parser.add_argument("-myl", "--moreylables", action="store_true")
parser.add_argument("-pr", "--plusratio", action="store_true")
parser.add_argument("-ppr", "--pluspadratio", default=0.3, type=float)
parser.add_argument("-r", "--ratio", action="store_true")
parser.add_argument("-rbe", "--ratiobinomialerr", action="store_true")
parser.add_argument("-rl", "--ratiolegend", action="store_true")
parser.add_argument("-rlp", "--ratiolegendposition", nargs =2, default=[0.5,0.8], type=float) #Defines top left corner of TLegend
parser.add_argument("-xrr", "--xratiorange", nargs=2, type=float)
parser.add_argument("-yrr", "--yratiorange", nargs=2, type=float)


#parser.add_argument("-", "--")

filelist = ()
filelegend = ()
ratiolegend = ()
skipmarker = ()
ratioskipmarker = ()
skipratio = ()

ratiobase = -1
counter = 0

config_line = ''

filecheck = ['-f ','--filename ']

with open(sys.argv[1],'r') as f:    #path to file with config of plot
    for li in f:
        if any ([x in li for x in filecheck]):
            lineargs = fileparser.parse_args(li.split())
            filelist +=(lineargs.filename, lineargs.numbercolumns),
            filelegend +=(lineargs.legend),
            ratiolegend +=(lineargs.ratiolegend),
            skipmarker +=(lineargs.nomarker),
            ratioskipmarker +=(lineargs.rationomarker),
            skipratio +=(lineargs.skipratio),
            if lineargs.ratiodivisor:
                ratiobase = counter
            counter += 1
        else:
            li = li.strip()
            li = li.strip('\n')
            if '-' in li:
                config_line += li 
                config_line += ' '
            else:
                print ('Line \"' + li +'\" does not start with an option for a variable')
            print config_line


config = parser.parse_args(config_line.split())
#print config


########## ROOT config

font2use = 43
fontsize = 20*config.markersize

ROOT.gStyle.SetTextFont(font2use)
ROOT.gStyle.SetTitleFontSize(fontsize)

ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetPadLeftMargin(config.leftmargin)
ROOT.gStyle.SetPadRightMargin(config.rightmargin)
ROOT.gStyle.SetPadTopMargin(config.topmargin)
ROOT.gStyle.SetPadBottomMargin(config.bottommargin)
ROOT.gStyle.SetTitleOffset(config.titleoffsety,"y")
ROOT.gStyle.SetTitleOffset(config.titleoffsetx,"x")
ROOT.gStyle.SetLabelFont(font2use,"x")
ROOT.gStyle.SetLabelFont(font2use,"y")
ROOT.gStyle.SetLabelSize(fontsize,"x")
ROOT.gStyle.SetLabelSize(fontsize,"y")
ROOT.gStyle.SetTitleFont(font2use,"x")
ROOT.gStyle.SetTitleFont(font2use,"y")
ROOT.gStyle.SetTitleYSize(fontsize)
ROOT.gStyle.SetTitleXSize(fontsize)

if config.alternativecolors:
    markertable = {0:[ROOT.kBlue+2,33,1.7],1:[ROOT.kOrange+10,8,1.0],2:[ROOT.kTeal-6,21,1.0],3:[ROOT.kMagenta+3,34,1.4],4:[ROOT.kBlue+2,22,1.2],5:[ROOT.kPink,23,1.2],6:[ROOT.kOrange+10,29,1.6],7:[ROOT.kTeal+3,21,1.0]}
else:
    markertable = {0:[ROOT.kAzure+2,33,1.7],1:[ROOT.kSpring-8,8,1.0],2:[ROOT.kRed+1,21,1.0],3:[ROOT.kOrange+1,34,1.4],4:[ROOT.kAzure+2,22,1.2],5:[ROOT.kSpring-8,23,1.2],6:[ROOT.kRed+1,29,1.6],7:[ROOT.kOrange+1,21,1.0]}


#print config
#print filelist

########## General input

FileBinning = open(config.filebinning,'r')

BinEdges = []
for li in FileBinning:
    splitline = li.split()
    BinEdges.append(float(splitline[0]))
    #print splitline[0]

BinRange = [min(BinEdges),max(BinEdges)]

print BinRange

NBins = BinEdges[0:len(BinEdges)-1]

Bins = []
Ex = []

for i in range(len(BinEdges)-1):
    Bins.append((BinEdges[i]+BinEdges[i+1])/2)

print NBins
print BinEdges
print Bins
ex = np.zeros(len(NBins))

#print len(BinEdges)

########## Data point input

#FillValues = np.zeros((len(filelist),len(BinEdges)-1), dtype=object)
FillValues = []

for i in range (len(filelist)):
    FillValues.append(Read_Data(filelist[i]))
    print filelist[i]


########## General histogram
TCspectrum = ROOT.TCanvas("TCspectrum","",20,20,config.sizex,config.sizey)
if config.tgrapherrors:
    #TmultiGraph
    TH1Plot = ROOT.TH1D("TH1Plot",config.title,len(NBins),np.array(BinEdges,'d'))
else:
    THSt1 = ROOT.THStack("THStack1",config.title)
    TH1Plot = []

if config.ratio or config.plusratio:
    THSRatio = ROOT.THStack("THSRatio","%s_ratio"%(config.title))

if config.xlog:
    ROOT.gPad.SetLogx()
if config.ylog:
    ROOT.gPad.SetLogy()

if config.legendtitle:
    TLeg = ROOT.TLegend(config.legendposition[0],config.legendposition[1],config.legendposition[0]+0.05,config.legendposition[1]-(len(filelist)+1)*(0.02*config.markersize))
else:
    TLeg = ROOT.TLegend(config.legendposition[0],config.legendposition[1],config.legendposition[0]+0.05,config.legendposition[1]-len(filelist)*(0.02*config.markersize))
TLeg.SetFillColor(0)
TLeg.SetMargin(0.075*config.markersize)
TLeg.SetBorderSize(0)
TLeg.SetTextFont(font2use)
TLeg.SetTextSize(fontsize)
if config.legendtitle:
    TLeg.AddEntry("", "  %s"%(' '.join(config.legendtitle)),"")

if config.label:
    print config.labelbox
    Label = ROOT.TLegend(config.labelbox[0],config.labelbox[1],config.labelbox[2],config.labelbox[3])
    Label.SetFillColor(0)
    Label.SetBorderSize(0)
    Label.SetTextFont(font2use)
    Label.SetTextSize(fontsize)
    Label.AddEntry("","%s"%(' '.join(config.label)),"")
    

for i in range(0,len(FillValues)):
    if config.tgrapherrors:
        TGE1 = ROOT.TGraphErrors(len(Bins),np.array(Bins,'d'),unumpy.nominal_values(FillValues[i]),ex,unumpy.std_devs(FillValues[i]))
        TGE1.SetMarkerColor(markertable.get(i)[0])
        TGE1.SetMarkerStyle(markertable.get(i)[1])
        TGE1.SetMarkerSize(markertable.get(i)[2]*config.markersize)
        if ( len(BinEdges)-1 != len(FillValues[i]) ) :
            sys.exit( "Size of binning and number of values don't agree. Stopping macro!")
        TLeg.AddEntry(TGE1, ("  %s"%(' '.join(filelegend[i]))))
    else:
        TH1Plot.append(ROOT.TH1D("TH1Plot","%i"%(i),len(NBins),np.array(BinEdges,'d')))
        TH1Plot[i].SetContent(unumpy.nominal_values(FillValues[i]))
        TH1Plot[i].SetError(unumpy.std_devs(FillValues[i]))
        TH1Plot[i].SetMarkerColor(markertable.get(i)[0])
        TH1Plot[i].SetMarkerStyle(markertable.get(i)[1])
        TH1Plot[i].SetMarkerSize(markertable.get(i)[2]*config.markersize)
        if ( len(BinEdges) != len(FillValues[i]) ) :
            sys.exit( "Size of binning and number of values don't agree. Stopping macro!")
        THSt1.Add(TH1Plot[i])
        if skipmarker[i]:
            TLeg.AddEntry("", ("  %s"%(' '.join(filelegend[i]))),"")
        else:
            TLeg.AddEntry(TH1Plot[i], ("  %s"%(' '.join(filelegend[i]))))
    
    
if config.tgrapherrors:
    TH1Plot.GetXaxis().SetTitle(config.xtitle)
    TH1Plot.GetYaxis().SetTitle(config.ytitle)
    if config.xrange:
        TH1Plot.GetXaxis().SetRangeUser(config.xrange[0],config.xrange[1])
    if config.yrange:
        TH1Plot.GetYaxis().SetRangeUser(config.yrange[0],config.yrange[1])
else:
    if config.stack:
        THSt1.Draw("")
    else:
        THSt1.Draw("nostack")
    THSt1.GetXaxis().SetTitle("%s"%(' '.join(config.xtitle)))
    THSt1.GetYaxis().SetTitle("%s"%(' '.join(config.ytitle)))
    if config.xrange:
        THSt1.GetXaxis().SetRangeUser(config.xrange[0],config.xrange[1])
        print "set x-range"
    if config.yrange:
        THSt1.SetMinimum(config.yrange[0])
        THSt1.SetMaximum(config.yrange[1])
        print "set y-range"
    if config.morexlables:
        THSt1.GetXaxis().SetMoreLogLabels(True)


########## Plot spectrum

if config.tgrapherrors:
    try:
        TH1Plot.DrawCopy()
        TGE1.Draw("sameP")
    except:
        pass
else:
    if config.stack:
        THSt1.Draw("")
    else:
        THSt1.Draw("nostack")

#TLeg = TC1.BuildLegend()
#TLeg.AddEntry("","test", "")
TLeg.Draw("")

if config.label:
    Label.Draw("")



########## Ratio histogram

if  config.ratio or config.plusratio:
    THSRatio = ROOT.THStack("THStackRatio",config.title)
    
    TRatioLeg = ROOT.TLegend(config.ratiolegendposition[0],config.ratiolegendposition[1],config.ratiolegendposition[0]+0.25,config.ratiolegendposition[1]-(len(filelist)-1)*(0.02*config.markersize))
    TRatioLeg.SetFillColor(0)
    TRatioLeg.SetMargin(0.075*config.markersize)
    TRatioLeg.SetBorderSize(0)
    TRatioLeg.SetTextFont(font2use)
    TRatioLeg.SetTextSize(fontsize)

    TFconst1 = ROOT.TF1("TFconst1","1.",BinRange[0],BinRange[1])
    
    
    
    for i in range(0,len(FillValues)):
        print i
        THDiv=TH1Plot[i].Clone()
        THDiv.Sumw2
        if skipratio[i]:
            print "skip ratio for "
            continue
        if i == ratiobase:
            TFconst1.SetLineColor(markertable.get(i)[0])
            TFconst1.SetLineWidth(4)
            TRatioLeg.AddEntry(TFconst1, ("  %s"%(' '.join(ratiolegend[i]))),"l")
            print "draw const for "
            continue
        if config.ratiobinomialerr:
            THDiv.Divide(TH1Plot[i],TH1Plot[ratiobase],1.,1.,"B")
            print "Bionmial errors used"
        else:
            THDiv.Divide(TH1Plot[i],TH1Plot[ratiobase])
        if ratioskipmarker[i]:
            TRatioLeg.AddEntry("", ("  %s"%(' '.join(ratiolegend[i]))),"")
        else:
            TRatioLeg.AddEntry(TH1Plot[i], ("  %s"%(' '.join(ratiolegend[i]))),"p")
        THSRatio.Add(THDiv)
    
    
    TCratio = ROOT.TCanvas("TCratio","",20,20,config.sizex,config.sizey)
    THSRatio.Draw("nostack")
    THSRatio.GetXaxis().SetTitle("%s"%(' '.join(config.xtitle)))
    if config.xratiorange:
        THSRatio.GetXaxis().SetRangeUser(config.xratiorange[0],config.xratiorange[1])
        print "set x-range"
    
    if config.yratiorange:
        THSRatio.SetMinimum(config.yratiorange[0])
        THSRatio.SetMaximum(config.yratiorange[1])
        print "set y-range"
    
    
    ########## Plot ratio
    
    if config.ratio:
        TFconst1.Draw("same")
        THSRatio.Draw("nostacksame")
    if config.ratiolegend:
        TRatioLeg.Draw("")

    ########## Plot spectrum + ratio

    if config.plusratio:
        TCplus = ROOT.TCanvas("TCplus","",20,20,config.sizex,config.sizey)
        TCplus.Divide(1,2)
        TCplus.cd(1).SetPad(0., config.pluspadratio, 1., 1.);  # top pad
        TCplus.cd(1).SetBottomMargin(0.001);
        TCplus.cd(2).SetPad(0., 0., 1., config.pluspadratio);  # bottom pad
        TCplus.cd(2).SetTopMargin(0);
        TCplus.cd(2).SetBottomMargin(config.bottommargin/config.pluspadratio); # for x-axis label
        
        TLegPlus = TLeg.Clone("TLegPlus")
        if config.legendtitle:  #Extend legend size due to shrinked canvas. NEED TO RESET Y1 instead of Y2, because TBox orders Y1 and Y2 by size and the legend position is defined by the top left corner (Y1 > Y2).
            TLegPlus.SetY1(config.legendposition[1]-((len(filelist)+1)*(0.02*config.markersize))/(1-config.pluspadratio))
            #TLegPlus.SetY2(config.legendposition[1]-((len(filelist)+1)*(0.02*config.markersize)))
        else:
            TLegPlus.SetY1(config.legendposition[1]-(len(filelist)*(0.02*config.markersize))/(1-config.pluspadratio))
            #TLegPlus.SetY2(config.legendposition[1]-(len(filelist)*(0.02*config.markersize)))
        
    
        TCplus.cd(1)
        if config.xlog:
            ROOT.gPad.SetLogx()
        if config.ylog:
            ROOT.gPad.SetLogy()
        THSt1.Draw("nostack")
        #TLegPlus.SetY2(0.0)
        TLegPlus.Draw("")
        if config.label:
            Label.Draw("")
        
        TCplus.cd(2)
        THSRatio.GetXaxis().SetTitleOffset(config.titleoffsetx/config.pluspadratio)
        THSRatio.Draw("nostack")
        TFconst1.Draw("same")
        THSRatio.Draw("nostacksame")
        #TRatioLeg.Draw("")
        #if config.ratio:
        #    THSRatio.DrawCopy("nostacksame")
        #if config.ratiolegend:

        
    
Save_Plots()

