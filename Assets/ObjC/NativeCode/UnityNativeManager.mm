//
//  UnityCallbacks.m
//  Unity-iPhone
//
//  Created by Juan-Manuel Fluxà on 8/6/10.
//  Copyright 2010 ReignDesign. All rights reserved.
//

// --- Mono / Unity Bridge ------------------------------------------------------
//

#import "UnityNativeManager.h"

static UnityNativeManager *sharedManager = nil;

void UnityPause(bool pause);

extern "C" {
	
	typedef void* MonoDomain;
	typedef void* MonoAssembly;
	typedef void* MonoImage;
	typedef void* MonoClass;
	typedef void* MonoObject;
	typedef void* MonoMethodDesc;
	typedef void* MonoMethod;
	typedef void* MonoString;
	typedef int gboolean;
	typedef void* gpointer;
	
	MonoDomain *mono_domain_get();
	MonoAssembly *mono_domain_assembly_open(MonoDomain *domain, const char *assemblyName);
	MonoImage *mono_assembly_get_image(MonoAssembly *assembly);
	MonoMethodDesc *mono_method_desc_new(const char *methodString, gboolean useNamespace);
	MonoMethodDesc *mono_method_desc_free(MonoMethodDesc *desc);
	MonoMethod *mono_method_desc_search_in_image(MonoMethodDesc *methodDesc, MonoImage *image);
	MonoObject *mono_runtime_invoke(MonoMethod *method, void *obj, void **params, MonoObject **exc);
	MonoClass *mono_class_from_name(MonoImage *image, const char *namespaceString, const char *classnameString);
	MonoMethod *mono_class_get_methods(MonoClass*, gpointer* iter);
	MonoString *mono_string_new(MonoDomain *domain, const char *text);
	char* mono_method_get_name (MonoMethod *method);
    
    MonoDomain *domain;
	NSString *assemblyPath;
	MonoAssembly *monoAssembly;
	MonoImage *monoImage;
    
	MonoMethodDesc *opponentDataDesc;
	MonoMethod *opponentDataMethod;
    
	MonoMethodDesc *connectionAliveDec;
	MonoMethod *connectionAliveMethod;
    
	MonoMethodDesc *manageAcceptedInviteDec;
	MonoMethod *manageAcceptedInviteMethod;
    
	MonoMethodDesc *setGameCenterAvilableDec;
	MonoMethod *setGameCenterAvilableMethod;
    
	MonoMethodDesc *setGameCenterLocalAliasDec;
	MonoMethod *setGameCenterLocalAliasMethod;
    
	MonoMethodDesc *getPlayerInfoDec;
	MonoMethod *getPlayerInfoMethod;

}



@implementation UnityNativeManager

@synthesize navigationControler;

+ (UnityNativeManager*)sharedManager
{
	
	if( !sharedManager )
		sharedManager = [[UnityNativeManager alloc] init];
	
	return sharedManager;
}

//blablabla

@end
