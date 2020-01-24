%% Clear Workstation
close all;
clear all;

%% Read Data (CSV File)
data = csvread('England.csv'); % England - Premier Leage CSV File

%% Format (Xs)
shortpasses=data(:,1);   % shortpasses
longpasses=data(:,2);  % long passes
totalpasses=data(:,3); % totalpasses
offensiveduels=data(:,4);  % offensive duels
defensiveduels=data(:,5); % defenive duels
fouls=data(:,6);  % fouls
offsides=data(:,7);   % offisdes
shots=data(:,8);   % long shots
freekicks=data(:,9);  % freekicks
touches=data(:,10);   % touches

%% Format (Y)
wins=data(:,11); % number of wins
%% 1. Model and Variables
plotmatrix(data) % Check for outliers + plot Xs against each other and against Y

%% 2. MLR Parameter Estimations and Confidence Intervals + 3. Test for Significance of Regression
% Linear model fit
X=[shortpasses, longpasses, totalpasses, offensiveduels, defensiveduels, fouls, offsides, shots, freekicks, touches];
mdl1=fitlm(X,wins,'VarNames',{'shortpasses','longpasses','totalpasses','offensiveduels','defensiveduels','fouls','offsides','shots','freekicks','touches','wins'}); 
figure
plot(mdl1)

% Confidence Intervals (From md11)
beta=[-8.4226,0.069249,-0.16806,-0.042782,0.019996,-0.086734, -0.18683,3.4759,0.36491, 0.087307,0.31634];
SE=[41.696,0.43809,0.85817,0.44956,0.28411,0.29333,1.4635,2.3721,1.2337,0.76939,0.44604];
tinv=2.2622;
upper=beta+tinv*SE;
lower=beta-tinv*SE;
upper
lower

%% 3. Final Model Building (Multiple Models - See Report for Justification) 
[b,se,pval,inmodel,stats,nextstep,history]= stepwisefit(X,wins); % Stepwise fit - to determine most significant predictor(s)
Xoffense=[shortpasses, longpasses, totalpasses, offensiveduels, offsides, shots, freekicks, touches]; % Offensive predictors
mdl2=fitlm(Xoffense,wins,'VarNames',{'shortpasses','longpasses','totalpasses','offensiveduels','offsides','shots','freekicks','touches','wins'});
mdl2

Xdefense=[defensiveduels,fouls]; % Defensive predictors
mdl3=fitlm(Xdefense,wins,'VarNames',{'defensiveduels','fouls','wins'});
mdl3

X6=[longpasses,shots,offensiveduels,freekicks]; % Aggressive offense
mdl6=fitlm(X6,wins,'VarNames',{'longpasses','shots','offensiveduels','freekicks','wins'});
mdl6

Xultimate=[shortpasses,shots,defensiveduels]; % Consisently significant predictors
mdlultimate=fitlm(Xultimate,wins,'VarNames',{'shortpasses','shots','defensiveduels','wins'});
mdlultimate
%% 5. Analysis of Residuals
r = mdl1.Residuals.Raw;
figure
histogram(r)
title('Histogram of Residuals');

figure
normplot(r)
title('Normplot of Residuals');

figure
plotmatrix([shortpasses, longpasses, totalpasses, offensiveduels, defensiveduels, fouls, offsides, shots, freekicks, touches],r)
title('Xs vs Residuals');

figure
yhat = mdl1.Fitted;
plotmatrix([wins yhat],r)
title('Predicted Values vs Residuals');
