% script2.m
% Generation, representation and playback of STEREO (multichannel) sounds

Fs = 16000; Ts = 1/Fs;
time = 0:Ts:1;

% Signal Generation
xLeft = cos(2*pi*250*time)';   % Left Channel
xRight = cos(2*pi*450*time)';  % Right Channel
x = [xLeft xRight];            % Compose STEREO signal

% Plot x;
figure;
subplot(2,1,1); plot(time, x(:,1)); xlabel('Time (sec)'); title('Left Channel');
subplot(2,1,2); plot(time, x(:,2)); ylabel('Time (sec)'); title('Right Channel');

% Play Sound
sound(x, Fs);