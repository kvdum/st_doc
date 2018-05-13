clear all
disp('ANT: running calc:')
%syms tau t_n c_v I_i c_sgk K_sgk G_sgk t_sgk c_gk_i G_gk_i K_gk_i t_1_gk_i t_2_gk_i t_gk_i G_I S_I H_I c_I_2 K_I_2 t_I_2 k_B F_B c_I_to t_I_to c_II_to K_II_to t_II_to G_IIc_II_1 K_II_1 c_II_2 K_II_2 t_II_2 G_x t_x c_1 K_1 t_1 c_2 K_2 t_2 c_3 K_3 t_3 c_m2 K_m2 t_m2 G_p t_p
syms tau t_n c_v I_i c_sgk K_sgk G_sgk t_sgk c_gk_i G_gk_i K_gk_i t_1_gk_i t_2_gk_i t_gk_i G_I S_I H_I c_I_2 K_I_2 t_I_2 k_B F_B c_I_to t_I_to c_II_to K_II_to t_II_to G_IIc_II_1 K_II_1 c_II_2 K_II_2 t_II_2 G_x t_x c_1 K_1 t_1 c_m2 K_m2 t_m2 G_p t_p

disp('Відображення введених рівнянь:')
eq1 = 'Dt_gk_i - (I_i-(G_gk_i * c_v * (t_1_gk_i - t_2_gk_i) + K_gk_i * (t_gk_i(tau) - t_n))) / c_gk_i'

eq2 = 'Dt_sgk - (G_I * c_v * (t_gk_i(tau) - t_sgk(tau)) - (K_sgk * (t_sgk(tau) - t_n) + G_I * c_v * (t_sgk(tau) - t_I_to(tau)) )) /  c_sgk'

eq3 = 'Dt_I_to - G_I * (1 - smp_exp((-k_B*F_B)/G_p)) / c_I_to'

eq4 = 'Dt_I_2 - (G_I * c_v * (t_I_to(tau) - t_I_2(tau)) - K_I_2 * (t_I_to(tau) - t_n)) / c_I_2'

eq5 = 'Dt_II_2 - (G_II * c_v * (t_m2(tau) - t_II_2(tau)) - K_II_2 * (t_II_2(tau) - t_n)) / c_II_2'

eq6 = 'Dt_II_to - (G_I * c_v * (t_II_to(tau) - t_I_2(tau)) - (K_II_to * (t_II_to(tau) - t_n) + G_II * c_v * (t_II_to(tau) - t_II_2(tau)))) / c_II_to'

eq7 = 'Dt_II_1 - (G_II * c_v * (t_II_to(tau) - t_II_1(tau)) - (K_II_1 * (t_II_1(tau) - t_n) + G_II * c_v * (t_II_1(tau) - t_1(tau)))) / c_II_1'

eq8 = 'Dt_1 - (G_II * c_v * (t_II_2(tau) - t_1(tau)) - K_1 * (t_1(tau) - t_n) + G_p * c_v * (t_1(tau) - t_p)) / c_1'

%eq9 = 'Dt_2 - (G_II * c_v * (t_1(tau) - t_2(tau)) - K_2 * (t_2(tau) - t_n)) / c_2'

%eq10 = 'Dt_3 - (G_II * c_v * (t_2(tau) - t_3(tau)) - K_3 * (t_3(tau) - t_n)) / c_2'

%eq11 = 'Dt_m2 - (G_II * c_v * (t_3(tau) - t_m2(tau)) + G_x * c_v * (t_x - t_m2(tau)) - K_m2 * (t_m2(tau) - t_n)) / c_m2'
eq11 = 'Dt_m2 - (G_II * c_v * (t_1(tau) - t_m2(tau)) + G_x * c_v * (t_x - t_m2(tau)) - K_m2 * (t_m2(tau) - t_n)) / c_m2'

disp('Визначення результату...')
%res = dsolve(eq1, eq2, eq3, eq4, eq5, eq6, eq7, eq8, eq9, eq10, eq11, tau);
res = dsolve(eq1, eq2, eq3, eq4, eq5, eq6, eq7, eq8, eq11, tau);
pretty(res.t_gk_i)
pretty(res.t_sgk)
pretty(res.t_I_to)
pretty(res.t_I_2)
pretty(res.t_II_2)
pretty(res.t_II_to)
pretty(res.t_II_1)
pretty(res.t_1)
%pretty(res.t_2)
%pretty(res.t_3)
pretty(res.t_m2)