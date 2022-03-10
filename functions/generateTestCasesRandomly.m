function testSuite = generateTestCasesRandomly(nTestCases)
    for ii=1:nTestCases
        try
           [refPose,rute]=generateWay(randi([1 51]),randi([1 51]),1);
        catch 
           [refPose,rute]=generateWay(randi([1 51]),randi([1 51]),1);
        end
        
        points=ReadMapPoints();
        points=table2array(points);
        xRef = refPose(:,1);
        yRef = -refPose(:,2); 
        
        testSuite{ii}.rute=rute;
        testSuite{ii}.points=points;
        testSuite{ii}.refPose = refPose;
        testSuite{ii}.xRef = xRef;
        testSuite{ii}.yRef = yRef;
        testSuite{ii}.distance=getDistance(xRef,yRef);
        testSuite{ii}.nominalSpeed = randi([6 12]); %[6-12]
        testSuite{ii}.minimalSpeed = randi([1 4]); %[0.5-4]
        testSuite{ii}.angVelGain = randi([0 100]); %[0-100]
        testSuite{ii}.approximationReductionGain =  0.2 + (3-0.2) * rand; %[0.2-3] ?
        testSuite{ii}.l=randi([1 7]);%[1-7]
        testSuite{ii}.ld=randi([4 8]);%[4-8]
        testSuite{ii}.slopeX1=0;
        testSuite{ii}.slopeX2=0;
        testSuite{ii}.slopeY1=0;
        testSuite{ii}.slopeY2=0;
        testSuite{ii}.X1=-242.0000;
        testSuite{ii}.X2=-242.0000;
        testSuite{ii}.Y1=-153.6700;
        testSuite{ii}.Y2=-153.6700;
        testSuite{ii}.psi1=yawCalculator(testSuite{ii}.X1,testSuite{ii}.Y1,testSuite{ii}.X1+testSuite{ii}.slopeX1,-(testSuite{ii}.Y1+testSuite{ii}.slopeY1));
        testSuite{ii}.psi2=yawCalculator(testSuite{ii}.X2,testSuite{ii}.Y2,testSuite{ii}.X2+testSuite{ii}.slopeX2,-(testSuite{ii}.Y2+testSuite{ii}.slopeY2));
        
    end
end