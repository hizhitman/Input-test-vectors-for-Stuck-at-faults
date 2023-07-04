<Qucs Schematic 0.0.19>
<Properties>
  <View=0,0,800,800,1,0,0>
  <Grid=10,10,1>
  <DataSet=gh.dat>
  <DataDisplay=gh.dpl>
  <OpenDisplay=1>
  <Script=gh.m>
  <RunScript=0>
  <showFrame=0>
  <FrameText0=Title>
  <FrameText1=Drawn By:>
  <FrameText2=Date:>
  <FrameText3=Revision:>
</Properties>
<Symbol>
</Symbol>
<Components>
  <AND Y1 1 170 250 -26 27 0 0 "2" 0 "1 V" 0 "0" 0 "10" 0 "old" 0>
  <XOR Y3 1 520 300 -26 27 0 0 "2" 0 "1 V" 0 "0" 0 "10" 0 "old" 0>
  <Inv Y4 1 330 370 -26 27 0 0 "1 V" 0 "0" 0 "10" 0 "old" 0>
  <OR Y2 1 180 380 -26 27 0 0 "2" 0 "1 V" 0 "0" 0 "10" 0 "old" 0>
  <.Digi Digi1 1 250 610 0 51 0 0 "TruthTable" 1 "10 ns" 0 "Verilog" 0>
  <DigiSource S2 1 70 300 -35 16 0 0 "2" 1 "low" 0 "1ns; 1ns" 0 "1 V" 0>
  <DigiSource S3 1 80 370 -35 16 0 0 "3" 1 "low" 0 "2ns; 1ns" 0 "1 V" 0>
  <DigiSource S4 1 80 580 -35 16 0 0 "4" 1 "low" 0 "4ns; 1ns" 0 "1 V" 0>
  <DigiSource S5 1 80 130 -35 16 0 0 "1" 1 "low" 0 "1ns; 1ns" 0 "1 V" 0>
</Components>
<Wires>
  <200 250 200 290 "" 0 0 0 "">
  <200 290 490 290 "net_e" 390 260 161 "">
  <490 310 490 370 "" 0 0 0 "">
  <360 370 490 370 "net_g" 450 340 66 "">
  <70 240 70 250 "" 0 0 0 "">
  <70 240 80 240 "" 0 0 0 "">
  <210 370 300 370 "net_f" 290 340 51 "">
  <210 370 210 380 "" 0 0 0 "">
  <80 240 140 240 "A" 140 210 27 "">
  <80 130 80 240 "" 0 0 0 "">
  <80 390 150 390 "D" 150 360 44 "">
  <80 390 80 580 "" 0 0 0 "">
  <70 260 140 260 "B" 150 230 49 "">
  <70 260 70 300 "" 0 0 0 "">
  <80 370 150 370 "C" 160 340 42 "">
  <550 300 550 300 "Z" 580 270 0 "">
</Wires>
<Diagrams>
</Diagrams>
<Paintings>
</Paintings>
