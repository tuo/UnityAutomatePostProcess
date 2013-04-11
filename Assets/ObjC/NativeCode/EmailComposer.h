//
//  EmailComposer.h
//  Pigrush
//
//  Created by Juan-Manuel Fluxà on 8/6/10.
//  Copyright 2010 ReignDesign. All rights reserved.
//

#import <MessageUI/MessageUI.h>
#import <MessageUI/MFMailComposeViewController.h>


@interface EmailComposer : UIViewController <MFMailComposeViewControllerDelegate>
{
	
}

- (void) emailComposeWithSubject:(NSString*)subject emailBody:(NSString *)body;

@end 