//
//  ViewController.m
//  oAuthTest
//
//  Created by Sebastian Romero on 15/01/16.
//  Copyright © 2016 Jet. All rights reserved.
//

#import "ViewController.h"
#import "ADALiOS/ADAuthenticationContext.h"

@interface ViewController (){
    ADAuthenticationContext* authContext;
    NSDictionary *settings;
    NSString *accessToken;
}
@property (weak, nonatomic) IBOutlet UILabel *labelToken;

@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view, typically from a nib.
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}


-(void) viewDidAppear:(BOOL)animated {
    [super viewDidAppear:animated];
    [self getToken:YES completionHandler:^(NSString *token) {
        accessToken = token;
        dispatch_async(dispatch_get_main_queue(), ^{
            self.labelToken.text = accessToken;
        });
    }];
}


- (IBAction)button:(id)sender {
    NSLog(@"URL ???? %@", [settings objectForKey:@"finalUrl"]);
    NSURL *todoRestApiURL = [[NSURL alloc]initWithString:[settings objectForKey:@"finalUrl"]];
    NSMutableURLRequest *request = [[NSMutableURLRequest alloc]initWithURL:todoRestApiURL];
    NSString *authHeader = [NSString stringWithFormat:@"Bearer %@", accessToken];
    [request addValue:authHeader forHTTPHeaderField:@"Authorization"];
    NSOperationQueue *queue = [[NSOperationQueue alloc]init];
    [NSURLConnection sendAsynchronousRequest:request queue:queue completionHandler:^(NSURLResponse *response, NSData *data, NSError *error) {
        NSString* serverResponse = [[NSString alloc] initWithData:data encoding:NSUTF8StringEncoding];
        NSLog(@"???? %@", serverResponse);
    }];
    
    
    /*NSURLSession *session = [NSURLSession sharedSession];
    [[session dataTaskWithURL:[NSURL URLWithString:[settings objectForKey:@"finalUrl"]]
            completionHandler:^(NSData *data, NSURLResponse *response, NSError *error) {
                
            }] resume];*/
    
    
}



- (void) getToken : (BOOL) clearCache completionHandler:(void (^) (NSString*))completionBlock {
    ADAuthenticationError *error;
    NSString *path = [[NSBundle mainBundle] pathForResource:@"settings" ofType:@"plist"];
    settings = [[NSDictionary alloc] initWithContentsOfFile:path];
    authContext = [ADAuthenticationContext authenticationContextWithAuthority:[settings objectForKey:@"authority"] error:&error];
    NSURL *redirectUri = [NSURL URLWithString:[settings objectForKey:@"redirectUri"]];
    if(clearCache){
        [authContext.tokenCacheStore removeAllWithError:nil];
    }
    [authContext acquireTokenWithResource:[settings objectForKey:@"resourceString"]
                                 clientId:[settings objectForKey:@"clientId"]
                              redirectUri:redirectUri
                          completionBlock:^(ADAuthenticationResult *result) {
                              if (AD_SUCCEEDED != result.status){
                                  NSLog(@"Error : ???? %@", result.error.errorDetails);
                              }
                              else{
                                  completionBlock(result.accessToken);
                              }
                          }];
}

@end
