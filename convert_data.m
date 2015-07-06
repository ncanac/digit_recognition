% Read in file
arg_list = argv();
filename = arg_list{1};
fid = fopen(filename, 'r');
data = [];
while (! feof(fid))
    [t,N] = fread(fid,[28,28],'uchar');
    data = [data; t(:)'];
endwhile
fclose(fid);
data = int8(data);

save('-ascii', [filename '.txt'], 'data');
