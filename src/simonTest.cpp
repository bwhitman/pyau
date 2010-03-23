/*
 *  simonTest.cpp
 *
 *  Created by simon on 14/03/09.
 *  Copyright 2009 . All rights reserved.
 *
 */

//#define DEBUG 1

#include <AudioToolbox/AudioToolbox.h>
#include <CoreAudio/CoreAudio.h>
#include "AHHost.h"
#include "AHUtils.h"
#include "FileSystemUtils.h"

#include <iostream>
using namespace std;

void print_host(AHHost &host)
{    
    for (int i=0; i<(int)host.GetTracks().size(); i++)
    {
        AHTrack* t = host.GetTracks()[i];
        cout << "track " << i << ": ";
        PrintCFStringRef(t->GetSynth()->GetName());
        list<AHAudioUnit*> effects = t->GetEffects();
        for ( list<AHAudioUnit*>::iterator it=effects.begin(); it != effects.end(); it++)
        {
            cout << " => [";
            PrintCFStringRef((*it)->GetName());
            cout << "]";
        }
        cout << endl;            
    }        
}

int main( int argc, const char* argv[] )
{
//    PrintAllAudioUnits();
    /*list<CAComponent> liste = GetMatchingCAComponents(CAComponentDescription('aufx'));
    list<CAComponent> liste2 = GetMatchingCAComponents(CAComponentDescription('aumf'));
    list<CAComponent> listes[] = {liste, liste2};
    for(int i=0; i<2; i++)
    {
        for (list<CAComponent>::iterator it = listes[i].begin(); it != listes[i].end(); it++)
        {
            CAComponentDescription desc = it->Desc();
            char type[5], subtype[5], manu[5];
            FileSystemUtils::OSType2str(desc.Type(), type);
            FileSystemUtils::OSType2str(desc.SubType(), subtype);
            FileSystemUtils::OSType2str(desc.Manu(), manu);
            cout << type << " " << subtype << " " << manu << " ";
            PrintCFStringRef(it->GetAUName()); cout << endl;
        }
        cout << endl;
    }*/

    
    AHHost host;
    AHTrack* track1 = host.AddTrack("kontakt 3");
    track1->Arm();
    print_host(host);
    
    track1->GetSynth()->LoadAUPresetFromFile("/Library/kontakt3_db/aupresets_usable/Violin ens 14 (fortepiano).aupreset");
    
    //string midifile = "/Users/simon/tmp/midis/69.mid";
    //string midifile_james = "/Users/simon/Libs/pygmy/pygmy/projects/timbre/audiounit_tests/james.mid";
    //host.LoadMidiFile(midifile);
    //host.Play();
    //sleep(10);
    //host.BounceToFile("/Users/simon/tmp/james.wav");
    
    while( true)
        sleep(10);
            
}