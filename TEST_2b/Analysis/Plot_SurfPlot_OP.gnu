#!/usr/bin/gnuplot -persist
#
#    
#    	G N U P L O T
#    	Version 4.2 patchlevel 4 
#    	last modified Sep 2008
#    	System: Linux 2.6.29.6-server-3mnb
#    
#    	Copyright (C) 1986 - 1993, 1998, 2004, 2007, 2008
#    	Thomas Williams, Colin Kelley and many others
#    
#    	Type `help` to access the on-line reference manual.
#    	The gnuplot FAQ is available from http://www.gnuplot.info/faq/
#    
#    	Send bug reports and suggestions to <http://sourceforge.net/projects/gnuplot>
#    
# set terminal x11 
# set output
set term post color solid enhanced font "Helvetica,20"
unset clip points
set clip one
unset clip two
set bar 1.000000
set border 31 front linetype -1 linewidth 1.000
set xdata
set ydata
set zdata
set x2data
set y2data
set timefmt x "%d/%m/%y,%H:%M"
set timefmt y "%d/%m/%y,%H:%M"
set timefmt z "%d/%m/%y,%H:%M"
set timefmt x2 "%d/%m/%y,%H:%M"
set timefmt y2 "%d/%m/%y,%H:%M"
set timefmt cb "%d/%m/%y,%H:%M"
set boxwidth
set style fill  empty border
set style rectangle back fc lt -3 fillstyle  solid 1.00 border -1
set dummy x,y
set format x "% g"
set format y "% g"
set format x2 "% g"
set format y2 "% g"
set format z "% g"
set format cb "% g"
set angles radians
unset grid
set key title ""
set key inside right top vertical Right noreverse enhanced autotitles nobox
set key noinvert samplen 4 spacing 1 width 0 height 0 
unset label
unset arrow
set style increment default
unset style line
unset style arrow
set style histogram clustered gap 2 title  offset character 0, 0, 0
unset logscale
set offsets 0, 0, 0, 0
set pointsize 1
set encoding default
unset polar
unset parametric
unset decimalsign
set view map
set samples 100, 100
set isosamples 10, 10
set surface
unset contour
set clabel '%8.3g'
set mapping cartesian
set datafile separator whitespace
unset hidden3d
set cntrparam order 4
set cntrparam linear
set cntrparam levels auto 5
set cntrparam points 5
set size ratio 0 1,1
set origin 0,0
set style data pm3d
set style function pm3d
set xzeroaxis linetype -2 linewidth 1.000
set yzeroaxis linetype -2 linewidth 1.000
set zzeroaxis linetype -2 linewidth 1.000
set x2zeroaxis linetype -2 linewidth 1.000
set y2zeroaxis linetype -2 linewidth 1.000
set ticslevel 0.5
set mxtics default
set mytics default
set mztics default
set mx2tics default
set my2tics default
set mcbtics default
set xtics border in scale 1,0.5 mirror norotate  offset character 0, 0, 0
set xtics autofreq 
set ytics border in scale 1,0.5 mirror norotate  offset character 0, 0, 0
set ytics autofreq 
set ztics border in scale 1,0.5 nomirror norotate  offset character 0, 0, 0
set ztics autofreq 
set nox2tics
set noy2tics
set cbtics border in scale 1,0.5 mirror norotate  offset character 0, 0, 0
set cbtics autofreq 
set title "" 
set title  offset character 0, 0, 0 font "" norotate
set timestamp bottom 
set timestamp "" 
set timestamp  offset character 0, 0, 0 font "" norotate
set rrange [ * : * ] noreverse nowriteback  # (currently [0.00000:10.0000] )
set trange [ * : * ] noreverse nowriteback  # (currently [-5.00000:5.00000] )
set urange [ * : * ] noreverse nowriteback  # (currently [-5.00000:5.00000] )
set vrange [ * : * ] noreverse nowriteback  # (currently [-5.00000:5.00000] )
set xlabel "" 
set xlabel  offset character 0, 0, 0 font "" textcolor lt -1 norotate
set x2label "" 
set x2label  offset character 0, 0, 0 font "" textcolor lt -1 norotate
set xrange [ * : * ] noreverse nowriteback  # (currently [-10.0000:10.0000] )
set x2range [ * : * ] noreverse nowriteback  # (currently [-10.0000:10.0000] )
set ylabel "" 
set ylabel  offset character 0, 0, 0 font "" textcolor lt -1 rotate by 90
set y2label "" 
set y2label  offset character 0, 0, 0 font "" textcolor lt -1 rotate by 90
set yrange [ * : * ] noreverse nowriteback  # (currently [-10.0000:10.0000] )
set y2range [ * : * ] noreverse nowriteback  # (currently [-10.0000:10.0000] )
set zlabel "" 
set zlabel  offset character 0, 0, 0 font "" textcolor lt -1 norotate
set zrange [ * : * ] noreverse nowriteback  # (currently [-10.0000:10.0000] )
set cblabel "" 
set cblabel  offset character 0, 0, 0 font "" textcolor lt -1 rotate by 90
set cbrange [ * : * ] noreverse nowriteback  # (currently [-10.0000:10.0000] )
set zero 1e-08
set lmargin  -1
set bmargin  -1
set rmargin  -1
set tmargin  -1
set locale "C"
#set pm3d explicit at b
#set pm3d scansautomatic
#set pm3d interpolate 1,1 flush begin noftriangles nohidden3d corners2color mean
#set pm3d corners2color c1 
set palette positive nops_allcF maxcolors 0 gamma 1.5 color model RGB 
set palette rgbformulae 7, 5, 15
set colorbox default
set colorbox vertical origin screen 0.9, 0.2, 0 size screen 0.05, 0.6, 0 front bdefault
set loadpath 
set fontpath 
set fit noerrorvariables
GNUTERM = "x11"
#set view 60, 20, 0.85, 1.1 
set yrange [0:0.375]
set xrange [0:1.2]
set xtics 0.00, 0.15, 1.35
set ytics 0.00, 0.075, 0.375
#set pm3d #at b
set ticslevel 0.1
#set title 'Synchronization for P=155'
set xlabel ' Scaled coupling strength {/Symbol a}/C '
set ylabel ' Scaled coupling strength {/Symbol b}/C '
set cblabel 'Reg'
set format cb '%.1f'
set cblabel 'Cross-correlation'
set term post color enhanced
set output './Output_2_coupled_nodes/Output_0001/OrderParameter/Correlation_SurfPlot_5.ps'
splot './Output_2_coupled_nodes/Output_0001/OrderParameter/Correlation_SurfPlot.dat' u ($1/133.5):($2/133.5):($3) notitle 
#w pm3d notitle
#,'./Output_2_coupled_nodes/Output_0001/OrderParameter/Correlation_SurfPlot.dat' u ($1/133.5):($2/133.5):($3) w l lt -1 lw 0.5 notitle
#    EOF
