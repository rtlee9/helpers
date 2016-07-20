# accepts a list of vectors of identical length and returns one vector with the first non-NA value
coalesce <- function(...) {
    # convert input arguments into a list of vectors
    input_list = list(...)
    # check that all input vectors are of same length
    vectorlength = length(input_list[[1]])
    for (j in 1:length(input_list)) {
        if(length(input_list[[j]]) != vectorlength) {
            if (length(input_list[[j]]) == 1) {
                input_list[[j]] <- rep(input_list[[j]][1], vectorlength)
            } else {
                stop(paste("Not all vectors are of same length. First vector length: ",vectorlength,". Vector #",j,"'s length: ",length(input_list[[j]]), sep=""))
                }
        }
    }
    # create a result vector to fill with first non-NA values
    result = rep(NA,vectorlength)
    # fill with first non-NA value
    for (i in 1:length(result)) {
        for (j in 1:length(input_list)) {
            if(!is.na(input_list[[j]][i])) {
                result[i] = input_list[[j]][i]
                break
            }
        }
    }
    return(result)
}