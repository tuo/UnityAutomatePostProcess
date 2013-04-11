    #!/usr/bin/python
import sys
import os

def process_app_controller_wrapper(appcontroller_filename, newContent, methodSignatures, valuesToAppend, positionsInMethod, contentToAppend=None):
    appcontroller = open(appcontroller_filename, 'r')
    lines = appcontroller.readlines()
    appcontroller.close()
    foundWillResignActive = False    
    foundIndex = -1
    for line in lines:         
        print line
        newContent += line
        for idx, val in enumerate(methodSignatures):
            print idx, val
            if (line.strip() == val):
                print "founded match method: " + val
                foundIndex = idx
                foundWillResignActive = True
        if foundWillResignActive :
            if positionsInMethod[foundIndex] == 'begin' and line.strip() == '{':
                print "add code to resign body"
                newContent += ("\n\t" + valuesToAppend[foundIndex] + "\n\n")
                foundWillResignActive = False
            if 	positionsInMethod[foundIndex] == 'end' and line.strip() == '}':
                newContent = newContent[:-3]
                newContent += ("\n\n\t" + valuesToAppend[foundIndex] + "\n")
                newContent += "}\n"
                foundWillResignActive = False
        if line.strip() == '@end' and (not contentToAppend is None):
                newContent = newContent[:-6]
                newContent += ("\n\n\t" + contentToAppend + "\n")
                newContent += "@end"                            
            
    print "-------done loop close stream and content: " + newContent                    
    appcontroller = open(appcontroller_filename, 'w')    
    appcontroller.write(newContent)
    appcontroller.close()        

def chartboostAndRevMob():
    return '''
    Chartboost *cb = [Chartboost sharedChartboost];
    cb.appId = @"XXXXX";
    cb.appSignature = @"XXXX";
    [cb startSession];
    [RevMobAds startSessionWithAppID:@"XXX"]; 
    '''
def importHeaders():
    return '''
#import "Appirater.h"
#import "RDGameCenterManager.h"
#import "Chartboost.h"
#import <RevMobAds/RevMobAds.h>
#import "FlurryAnalytics.h"
'''

def pushActionInstanceDeclaration():
    return '''
	NSString *deviceTokenString;
	NSString *deviceAlias;
	NSString *pushActionURL;    
    '''
def extraCodeToAddInAppControllerMMFile():
    return '''

- (void)connection:(NSURLConnection *)theConnection didFailWithError:(NSError *)error {
    [UIApplication sharedApplication].networkActivityIndicatorVisible = NO;
    UIAlertView *someError = [[UIAlertView alloc] initWithTitle:
                              @"Network error" message: @"Error registering with server"
													   delegate: self
											  cancelButtonTitle: @"Ok"
											  otherButtonTitles: nil];
    [someError show];
    [someError release];
    NSLog(@"ERROR: NSError query result: %@", error);

}

    '''
    
def touch_implementation(appcontroller_filename):
    # appcontroller = open(appcontroller_filename, 'w')
    # print(" process AppController.mm add imports header")
    newContent = importHeaders()
     
    #starting line of method {
    methodSignatures = []
    #value to append near }
    valueToAppend = []
	#position to add insert at the beginning o
    positionsInMethod = []
    
    methodSignatures.append('- (void)applicationWillEnterForeground:(UIApplication *)application')
    valueToAppend.append('[Appirater appEnteredForeground:YES];')
    positionsInMethod.append("end")

    methodSignatures.append('- (void) applicationDidBecomeActive:(UIApplication*)application')
    valueToAppend.append(chartboostAndRevMob())        
    positionsInMethod.append("end")
    
    methodSignatures.append('- (void) dealloc')
    valueToAppend.append(pushActionDealloc())        
    positionsInMethod.append("begin")

    process_app_controller_wrapper(appcontroller_filename, newContent, methodSignatures, valueToAppend, positionsInMethod, extraCodeToAddInAppControllerMMFile())    

def touch_header(appcontroller_filename):
    # appcontroller = open(appcontroller_filename, 'w')
    # print(" process AppController.mm add imports header")
    newContent = ''
    #starting line of method {
    methodSignatures = []
    #value to append near }
    valueToAppend = []
    positionsInMethod = []

    methodSignatures.append('@interface AppController : NSObject<UIAccelerometerDelegate, UIApplicationDelegate>')
    valueToAppend.append(pushActionInstanceDeclaration())
    positionsInMethod.append("begin")
    process_app_controller_wrapper(appcontroller_filename, newContent, methodSignatures, valueToAppend, positionsInMethod)    
