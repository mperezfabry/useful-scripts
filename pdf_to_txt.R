# install.packages("pdftools")
# install.packages("here")
library(pdftools)
library(here)

dir <- getwd()

pdfs <- list.files(dir, pattern = "\\.pdf$", full.names = TRUE)


for (f in pdfs) {
  #Print start status
  cat("Reading:", basename(f), "...\n")
  #Renames the pdf to a .txt file to save without overwriting.
  txt_file <- sub("\\.pdf$", ".txt", f)
  
  #Reads in the file, writes each line as a vector to the txt file, handles exceptions like corrupted or unreadable files. 
  txt <- tryCatch({
    content <- pdf_text(f)
    writeLines(content, txt_file, useBytes = TRUE)
    TRUE
  }, error = function(e) {
    cat("Error reading:", basename(f), "-", e$message, "\n")
    FALSE
  })
  
  #Saves the text file as the same name as the pdf it pulled from.
  if (txt) {
    cat("Saved text file:", basename(txt_file), "\n\n")
  }
}
