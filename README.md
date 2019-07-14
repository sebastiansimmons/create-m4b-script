## Single .m4b Audiobook Script

Script that turns multiple mp3 files into a single m4b (iTunes audiobook) format.


<code>python convert-audiobook.py \<directory\></code>
  will create a file, output.m4b, from every mp3 file in \<directory\>. The m4b format is what Apple uses for audiobooks. It is the only way (that I know of) to get an audiobook to work seemlessly with the Books app.
 
Planning to add to this as I listen to more audiobooks and grow more frustrated with adding metadata manually.

## Multi .m4b Audiobook Script

iTunes will recognize multiple files as the same "book" if they are linked via file metadata. 
<code>python convert-audiobook-group.py  \<directory\></code>
  will convert every mp3 file in a directory/directories to a corresponding .m4b. These files will all be the same audiobook when imported into itunes. 
