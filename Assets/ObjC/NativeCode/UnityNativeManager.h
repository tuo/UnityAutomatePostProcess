//
//  UnityCallbacks.h
//  Unity-iPhone
//
//  Created by Juan-Manuel Fluxà on 8/6/10.
//  Copyright 2010 ReignDesign. All rights reserved.
//



@interface UnityNativeManager : NSObject {
	
	UINavigationController *navigationControler;
	
}

@property (nonatomic, retain) UINavigationController *navigationControler;

+ (UnityNativeManager *) sharedManager;

- (void) showViewController:(UIViewController *)viewController;
- (void) hideViewControllerAndRestartUnity;
- (void) purchaseSuccess:(NSString *)data;
- (void) purchaseFail:(NSString *)message;
- (void) gameCenterAvailable:(BOOL)isAvailable;
- (void) gameCenterLocalAlias:(NSString *)localAlias;
- (void) userCancel;
- (void) returnWithMessage:(NSString *)message;
- (void) socialSucceedWithMessage:(NSString *)message;

- (void) matchmakerMatchFound;

- (void) matchReportHandShake:(NSString *)localAlias 
				  LocalRandom:(int)localRandom 
				OpponentAlias:(NSString *)opponentAlias 
			   OpponentRandom:(int)opponentRandom 
			  OpponentTagPos:(int)tagPos 
			 OpponentMPPoints:(int)mpPoints 
			 OpponentSkinMode:(int)skinMode;

- (void) matchStartCountDown:(int)count;
- (void) matchStartGame;
- (void) opponentPosition:(NSString *)position;
- (void) opponentDataWithParam1:(float)param1 Param2:(float)param2 Param3:(float)param3 Param4:(float)param4 Param5:(float)param5 Param6:(float)param6;
- (void) opponentGameOver:(int)score;
- (void) opponentRematchRequested;
- (void) manageAcceptedInvite;
- (void) getLocalPlayerInfo;
- (void) playerDisconnected;
- (void) purchaseWait;
- (void) unityPause;
- (void) unityUnpause;

- (void) flurryLogEvent:(NSString*)eventname;

-(void)windowsubviews;




@end
