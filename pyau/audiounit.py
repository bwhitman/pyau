# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.33
#
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _audiounit
import new
new_instancemethod = new.instancemethod
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'PySwigObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


class AUChain(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, AUChain, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, AUChain, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _audiounit.new_AUChain(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _audiounit.delete_AUChain
    __del__ = lambda self : None;
    def GetAUGraph(*args): return _audiounit.AUChain_GetAUGraph(*args)
    def SetInstrument(*args): return _audiounit.AUChain_SetInstrument(*args)
    def GetInstrument(*args): return _audiounit.AUChain_GetInstrument(*args)
    def SetOutput(*args): return _audiounit.AUChain_SetOutput(*args)
    def GetOutput(*args): return _audiounit.AUChain_GetOutput(*args)
    def AddEffect(*args): return _audiounit.AUChain_AddEffect(*args)
    def RemoveEffect(*args): return _audiounit.AUChain_RemoveEffect(*args)
    def GetEffectAt(*args): return _audiounit.AUChain_GetEffectAt(*args)
    def Start(*args): return _audiounit.AUChain_Start(*args)
    def Stop(*args): return _audiounit.AUChain_Stop(*args)
AUChain_swigregister = _audiounit.AUChain_swigregister
AUChain_swigregister(AUChain)

class AudioUnitWrapper(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, AudioUnitWrapper, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, AudioUnitWrapper, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _audiounit.new_AudioUnitWrapper(*args)
        try: self.this.append(this)
        except: self.this = this
    def LoadAUPresetFromFile(*args): return _audiounit.AudioUnitWrapper_LoadAUPresetFromFile(*args)
    def SaveAuPresetToFile(*args): return _audiounit.AudioUnitWrapper_SaveAuPresetToFile(*args)
    def GetParameterList(*args): return _audiounit.AudioUnitWrapper_GetParameterList(*args)
    __swig_destroy__ = _audiounit.delete_AudioUnitWrapper
    __del__ = lambda self : None;
AudioUnitWrapper_swigregister = _audiounit.AudioUnitWrapper_swigregister
AudioUnitWrapper_swigregister(AudioUnitWrapper)

class FileMidi2AudioGenerator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, FileMidi2AudioGenerator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, FileMidi2AudioGenerator, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _audiounit.new_FileMidi2AudioGenerator(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _audiounit.delete_FileMidi2AudioGenerator
    __del__ = lambda self : None;
    def Initialize(*args): return _audiounit.FileMidi2AudioGenerator_Initialize(*args)
    def GenerateAudio(*args): return _audiounit.FileMidi2AudioGenerator_GenerateAudio(*args)
    def LoadMidiFile(*args): return _audiounit.FileMidi2AudioGenerator_LoadMidiFile(*args)
    def LoadInstrument(*args): return _audiounit.FileMidi2AudioGenerator_LoadInstrument(*args)
FileMidi2AudioGenerator_swigregister = _audiounit.FileMidi2AudioGenerator_swigregister
FileMidi2AudioGenerator_swigregister(FileMidi2AudioGenerator)



