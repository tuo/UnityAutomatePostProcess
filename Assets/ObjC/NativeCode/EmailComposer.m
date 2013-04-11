//
//  EMailComposer.m
//  Pigrush
//
//  Created by Juan-Manuel Fluxà on 8/6/10.
//  Copyright 2010 ReignDesign. All rights reserved.
//


#import "EmailComposer.h"
#import "UnityNativeManager.h"


@implementation EmailComposer

#pragma mark public methods
- (void) emailComposeWithSubject:(NSString*)subject emailBody:(NSString *)body
{

	if ([MFMailComposeViewController canSendMail]){
			
		MFMailComposeViewController *composer = [[MFMailComposeViewController alloc] init];
		
		composer.mailComposeDelegate = self;
		
		[composer setSubject:subject];
		
		[composer setMessageBody:body isHTML:NO];
		
		[self presentModalViewController:composer animated:YES];
		
		[composer release];
			
	}else{
		NSLog(@"device cant send mails");
		[[UnityNativeManager sharedManager] hideViewControllerAndRestartUnity];
		[[UnityNativeManager sharedManager] userCancel];
	}
	
}

#pragma mark MFMailComposeViewControllerDelegate
- (void) mailComposeController:(MFMailComposeViewController *)controller didFinishWithResult:(MFMailComposeResult)result error:(NSError *)error
{
	
	NSLog(@"view will be removed");
	[self dismissModalViewControllerAnimated:YES];
	[[UnityNativeManager sharedManager] hideViewControllerAndRestartUnity];
	[[UnityNativeManager sharedManager] userCancel];
	
}

@end


