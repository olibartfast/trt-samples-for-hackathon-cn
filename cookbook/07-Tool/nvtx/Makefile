include $(TRT_COOKBOOK_PATH)/include/Makefile.inc

LDFLAG     += -lnvToolsExt

SOURCE_CPP  = $(shell find . -name '*.cpp' 2>/dev/null)
OBJ         = $(shell find . -name *.o 2>/dev/null)
DEP         = $(OBJ:.o=.d)
TARGET_EXE  = $(SOURCE_CPP:.cpp=.exe)

-include $(DEP)

all: $(TARGET_EXE)

%.exe: %.o
	$(NVCC) $(LDFLAG) -o $@ $+

%.o: %.cpp
	$(NVCC) $(CCFLAG) $(INCLUDE) -M -MT $@ -o $(@:.o=.d) $<
	$(NVCC) $(CCFLAG) $(INCLUDE) -Xcompiler -fPIC -o $@ -c $<

.PHONY: test
test:
	make clean
	make
	./$(TARGET_EXE) > result-C++.log

.PHONY: clean
clean:
	rm -rf ./*.d ./*.o ./*.so ./*.exe ./*.trt
