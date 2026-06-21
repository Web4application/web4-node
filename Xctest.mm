@interface Table : NSObject
@property (nonatomic, assign) NSInteger rowCount;
@property (nonatomic, assign) NSInteger columnCount;
@end

@implementation Table

- (instancetype)init {
    self = [super init];
    if (self) {
        _rowCount = 0;
        _columnCount = 0;
    }
    return self;
}

@end
