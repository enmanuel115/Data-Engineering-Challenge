CREATE DATABASE test
ON PRIMARY
     (NAME = 'test', FILENAME = 'D:\SQLData\test.mdf'),  
   FILEGROUP Static
     (NAME = 'test', FILENAME = 'c:\SQLData\test.ndf')
LOG ON 
   (NAME = 'testLog',  FILENAME = 'c:\SQLData\test.ldf')
go