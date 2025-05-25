import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:flutter_secure_storage/flutter_secure_storage.dart';

class ApiService {
  static const _baseUrl = 'http://192.168.1.7:8000';
  static const _storage = FlutterSecureStorage();
  static const baseUrl =
      'http://192.168.1.7:8000'; // Replace with your actual IP
  static const userId =
      '965b77ca-54c4-42f2-a9b1-a2f4d1d3b515'; // Hardcode for User1 for now

  static Future<bool> login(String username, String password) async {
    final url = Uri.parse('$_baseUrl/auth/login');
    final response = await http.post(
      url,
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({'username': username, 'password': password}),
    );

    if (response.statusCode == 200) {
      final data = jsonDecode(response.body);
      await _storage.write(key: 'access_token', value: data['access_token']);
      return true;
    } else {
      return false;
    }
  }

  static Future<String?> getToken() async {
    return await _st