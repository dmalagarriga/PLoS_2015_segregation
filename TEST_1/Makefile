####### Compiler, tools and options
TARGET = nmm.exe
SOURCES_DIR = Sources
HEADERS_DIR = Headers
OBJECTS_DIR = Objects

#C++ = mpic++
C++ = g++

MAIN = $(SOURCES_DIR)/$(TARGET:.exe=.cpp)

# Makes a list of the object (.o) files.
OBJECT_FILES = $(OBJECTS_DIR)/Parameters.o \
               $(OBJECTS_DIR)/voxel.o \
               $(OBJECTS_DIR)/Heun.o \
               $(OBJECTS_DIR)/rhsjansen.o 	
#               $(OBJECTS_DIR)/Get_New_Xs.o \
#               $(OBJECTS_DIR)/write_To_File.o

all: $(OBJECT_FILES)
	@$(C++) -Wall $(MAIN) $(OBJECT_FILES) -o $(TARGET) -lgsl -lgslcblas -lm -ffloat-store   

#	./$(TARGET)

# Clean
clean:
	rm -f *.exe *~ */*~ Objects/*.o

$(OBJECTS_DIR)/Parameters.o : $(SOURCES_DIR)/Parameters.cpp
	$(C++) -c $< -o $@

$(OBJECTS_DIR)/voxel.o : $(SOURCES_DIR)/voxel.cpp
	$(C++) -c $< -o $@

$(OBJECTS_DIR)/rhsjansen.o : $(SOURCES_DIR)/rhsjansen.cpp
	$(C++) -c $< -o $@

$(OBJECTS_DIR)/Heun.o : $(SOURCES_DIR)/Heun.cpp
	$(C++) -c $< -o $@

#$(OBJECTS_DIR)/Get_New_Xs.o : $(SOURCES_DIR)/Get_New_Xs.cpp
#	$(C++) -c $< -o $@

#$(OBJECTS_DIR)/write_To_File.o : $(SOURCES_DIR)/write_To_File.cpp
#	$(C++) -c $< -o $@
