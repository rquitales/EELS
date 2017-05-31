require(tcltk)

eels <- function(start = 0, end = 0) {
  filePath <- tclvalue(tkgetOpenFile())
  step = (end - start) / (length(datapoints)-1)
  datapoints <- as.vector(t(read.csv(filePath, sep = '\t', header = F)))
  datapoints <- datapoints[!is.na(datapoints)]
  
  savePath <- tclvalue(tkgetSaveFile(filetypes="{{XY File} {.xy}} {{TAB Separated File} {.txt}} {{Comma Separated File} {.csv}} {{All files} *}"))
  
  if (start == 0 & end == 0){
    df <- data.frame(y=datapoints)
  }
  
  if (start != 0 | end != 0){
    xaxis <- round(c(start + step * 0:(length(datapoints)-1)),digits=4)
    df <- data.frame(x = xaxis, y = datapoints)
  }
  
  if (substr(savePath,nchar(savePath)-2,nchar(savePath)) == "csv"){
    write.csv(df,file = savePath,row.names=FALSE)
  }
  else{
    write.table(df,file = savePath,row.names=FALSE,sep="\t")
  }
}

# tt <- tktoplevel()
# button.widget <- tkbutton(tt,text="Open File",command=eels)
# tkpack(button.widget)