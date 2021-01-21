import ROOT
import argparse

if __name__ == '__main__':

 ROOT.gROOT.SetBatch(ROOT.kTRUE)

 parser =  argparse.ArgumentParser(description='split_Tree')
 parser.add_argument('-i', '--input', dest='input', required=True, type=str)
 parser.add_argument('-d', '--dir', dest='dir', required=False, type=str) 
 args = parser.parse_args()

 #dir = "tagsDumper/trees" 
 dir = ""
 if args.dir!="": dir = args.dir
 
 output_name = args.input
 output_nameEven = output_name.replace('.root','_even.root')
 output_nameOdd = output_name.replace('.root','_odd.root')
 outfile_even = ROOT.TFile(output_nameEven, "RECREATE")
 outfile_odd = ROOT.TFile(output_nameOdd, "RECREATE")
 inFile = ROOT.TFile(args.input,"READ")

 outfile_even.cd() 
 print "Running on even events..."
 if dir!="":
   dir1 = inFile.Get("tagsDumper") 
   dir2 = dir1.Get("trees") 
   for key in dir2.GetListOfKeys():
    tree = inFile.Get(dir+"/"+key.GetName())
    print str(dir2)+"/"+key.GetName()
    outtree_even = tree.CloneTree(0)
    nentries = tree.GetEntries()
    for i in range(0, nentries):
       tree.GetEntry(i) 
       if i%2 == 0: outtree_even.Fill() 
    outtree_even.Write()
   outfile_even.Close()
 else:
   for key in inFile.GetListOfKeys():
    tree = inFile.Get(key.GetName())
    outtree_even = tree.CloneTree(0)
    nentries = tree.GetEntries()
    for i in range(0, nentries):
       tree.GetEntry(i) 
       if i%2 == 0: outtree_even.Fill() 
    outtree_even.Write()
   outfile_even.Close()

 outfile_odd.cd() 
 print "Running on odd events..."
 if dir!="":
   dir1 = inFile.Get("tagsDumper") 
   dir2 = dir1.Get("trees") 
   for key in dir2.GetListOfKeys(): 
    tree = inFile.Get(dir+"/"+key.GetName())
    outtree_odd = tree.CloneTree(0)
    nentries = tree.GetEntries()
    for i in range(0, nentries):
       tree.GetEntry(i) 
       if i%2 != 0: outtree_odd.Fill() 
    outtree_odd.Write()
   outfile_odd.Close()
 else:
   for key in inFile.GetListOfKeys():
    tree = inFile.Get(key.GetName())
    outtree_odd = tree.CloneTree(0)
    nentries = tree.GetEntries()
    for i in range(0, nentries):
       tree.GetEntry(i) 
       if i%2 != 0: outtree_odd.Fill() 
    outtree_odd.Write()
   outfile_odd.Close()     

