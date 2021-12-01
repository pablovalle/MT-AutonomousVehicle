function psi_o=yawCalculator(x_0,y_0,x_1,y_1)
x=x_1-x_0;
y=y_1-y_0;
    psi_o=atan2(y,x);
%     if abs(x_0)-abs(x_1)<=1 && abs(x_0)-abs(x_1)>=-1
%         if y_0<y_1
%             psi_o=pi*1/2;
%         else
%             psi_o=pi*3/2;
%         end
%     elseif x_0<x_1
%         psi_o=0;
%     else
%         psi_o=pi;
%     end
end