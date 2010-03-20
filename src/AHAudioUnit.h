/*
 *  AHAudioUnit.h
 *
 *  Created by simon on 19/03/09.
 *  Modified by Simon on march 16th 2010
 *
 * Represents an Audio Unit.
 */

/*
 
 basically wraps an audio unit, by simply subclassing the already-done "CAAudioUnit.h"
 
 */

#ifndef __AHAUDIOUNIT__
#define __AHAUDIOUNIT__

#include "CAAudioUnit.h"
//#include "AudioUnit/AudioUnit.h"
#include "AHParameter.h"
#include <string>
#include <list>


class AHAudioUnit : public CAAudioUnit
{
public:
	
	AHAudioUnit(const AUNode &inNode, const AudioUnit& inUnit):CAAudioUnit(inNode, inUnit)
    {}
    
    AHAudioUnit():CAAudioUnit(){}
	
	virtual void LoadAUPresetFromFile(std::string aupresetPath);
	virtual void SaveAUPresetToFile(std::string aupresetPath);
	
	virtual std::list<AHParameter> GetParameterList(AudioUnitScope scope, AudioUnitElement element);
		
//	virtual ~AudioUnitWrapper() {}
	
	CFStringRef GetName() {return Comp().GetAUName();}
	CFStringRef GetManu() {return Comp().GetAUManu();}
    
    bool GetView();
};

#endif